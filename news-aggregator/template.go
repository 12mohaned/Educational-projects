package main

import (
	"encoding/xml"
	"html/template"
	"io/ioutil"
	"net/http"
	"strings"
	"sync"
)

var waitgroup sync.WaitGroup
var washington_news News

type RecentNews struct {
	Link      [5]string
	NewsPaper string
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

/*
return the top 3 Recent News in the RecentNews Page
*/
func HomeHandler(w http.ResponseWriter, r *http.Request) {
	var news Sitemapindex
	var sub_news News
	var nyTimes_link string = "https://www.nytimes.com/sitemaps/new/sitemap.xml.gz"
	var TopNews [5]string
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
		TopNews[i] = sub_news.Locations[i]
	}

	Page := RecentNews{Link: TopNews, NewsPaper: "NeyWork Times"}
	template, _ := template.ParseFiles("Home.html")
	template.Execute(w, Page)
}

func NewsRoutine(Location string) {
	defer waitgroup.Done()
	resp, _ := http.Get(strings.TrimSpace(Location))
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &washington_news)
	resp.Body.Close()
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
	http.HandleFunc("/Home", HomeHandler)
	http.HandleFunc("/washingtonpost", washingtonpostAggregateHandler)
	http.HandleFunc("/nytimes", newyorkTimesAggregateHandler)
	http.ListenAndServe(":8000", nil)
}
