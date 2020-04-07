package main

import (
	"encoding/xml"
	"html/template"
	"io/ioutil"
	"net/http"
	"strings"
	"sync"

	"golang.org/x/net/html"
)

var waitgroup sync.WaitGroup
var washington_news News

type RecentNews struct {
	Link  string
	Title string
}
type NewsForm struct {
	Link      []string
	NewsPaper string
}

type Sitemapindex struct {
	Locations []string `xml:"sitemap>loc"`
}

type News struct {
	Locations []string `xml:"url>loc"`
}

type RecentSuperNews struct {
	Article [5]RecentNews
}

/*
return the top 5 Recent News in the RecentNews Page
*/
func HomeHandler(w http.ResponseWriter, r *http.Request) {
	var news Sitemapindex
	var sub_news News
	var nyTimes_link string = "https://www.nytimes.com/sitemaps/new/sitemap.xml.gz"
	var News [5]RecentNews
	var i int32

	resp, _ := http.Get(nyTimes_link)
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &news)
	resp.Body.Close()

	resp, _ = http.Get(news.Locations[0])
	bytes, _ = ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &sub_news)
	resp.Body.Close()

	for i = 0; i < 5; i++ {

		waitgroup.Add(1)
		go NewsRoutine(sub_news.Locations[i])
		var title string = StoreTitle(sub_news.Locations[i])
		if title != "error" {
			RN := RecentNews{Link: sub_news.Locations[i], Title: title}
			News[i] = RN

		} else {
			panic("This News Paper Doesn't Have a Title")
		}
	}
	waitgroup.Wait()

	Page := RecentSuperNews{Article: News}
	template, _ := template.ParseFiles("Home.html")
	template.Execute(w, Page)
}

/*
Return the Array washington_news which contains Link to all the Articles
*/
func NewsRoutine(Location string) {
	defer waitgroup.Done()
	resp, _ := http.Get(strings.TrimSpace(Location))
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &washington_news)
	resp.Body.Close()
}

/*
Store the Title of a Newspaper
*/
func StoreTitle(Location string) string {
	resp, _ := http.Get(strings.TrimSpace(Location))
	z := html.NewTokenizer(resp.Body)
	for {
		tt := z.Next()
		switch {
		case tt == html.ErrorToken:
			return "error"
		case tt == html.StartTagToken:
			token := z.Token()
			if "title" == token.Data {
				tt = z.Next()
				if tt == html.TextToken {
					return z.Token().Data
				}
			}
		}
	}

}

/*
Responsible for Generating SiteMaps of WashigntonPost on following topics ex :
Business, Entertainment, technology, world
*/
func washingtonpostAggregateHandler(w http.ResponseWriter, r *http.Request) {
	var washingtmainsitemap Sitemapindex
	var Washignton_link string = "https://www.washingtonpost.com/sitemaps/index.xml"
	resp, _ := http.Get(Washignton_link)
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &washingtmainsitemap)
	resp.Body.Close()
	var i int
	for i = 0; i < len(washingtmainsitemap.Locations); i++ {
		waitgroup.Add(1)
		go NewsRoutine(washingtmainsitemap.Locations[i])
	}
	waitgroup.Wait()
	Page := NewsForm{Link: washington_news.Locations, NewsPaper: "washingtonpost"}
	t, _ := template.ParseFiles("basictemplating.html")
	t.Execute(w, Page)
}

/*
Responsible for Generating SiteMaps of Ny-Times on following topics ex :
Business, Entertainment, technology, world
*/
func newyorkTimesAggregateHandler(w http.ResponseWriter, r *http.Request) {
	var nyTimes Sitemapindex
	var nyTimes_news News
	var nyTimes_link string = "https://www.nytimes.com/sitemaps/new/sitemap.xml.gz"
	resp, _ := http.Get(nyTimes_link)
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &nyTimes)
	resp.Body.Close()

	resp, _ = http.Get(strings.TrimSpace(nyTimes.Locations[0]))
	bytes, _ = ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &nyTimes_news)
	resp.Body.Close()

	Page := NewsForm{Link: nyTimes_news.Locations, NewsPaper: "NewYorkTimes"}
	t, _ := template.ParseFiles("basictemplating.html")
	t.Execute(w, Page)
}

func main() {
	http.HandleFunc("/News", HomeHandler)
	http.HandleFunc("/washingtonpost", washingtonpostAggregateHandler)
	http.HandleFunc("/nytimes", newyorkTimesAggregateHandler)
	http.ListenAndServe(":8080", nil)
}
