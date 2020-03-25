package main
import (
	"fmt"
	"html/template"
	"encoding/xml"
	"io/ioutil"
	"net/http"
	"strings"
)

type NewsForm struct {
	Link [] string
	NewsPaper string
}

type Sitemapindex struct {
	Locations []string `xml:"sitemap>loc"`
}

type News struct {
	Locations []string `xml:"url>loc"`
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "<h1>There is nothing here but a blank page go to the news</h1>")
}
/*
Responsible for Generating SiteMaps of WashigntonPost on following topics ex :
Business, Entertainment, technology, world
*/
func washingtonpostAggregateHandler(w http.ResponseWriter, r *http.Request) {
	var washingtmainsitemap Sitemapindex
	var washington_news News
	var Washignton_link string = "https://www.washingtonpost.com/sitemaps/index.xml"
	resp, _ := http.Get(Washignton_link)
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &washingtmainsitemap)
	resp.Body.Close()
	var i int
	for i =0; i < len(washingtmainsitemap.Locations);i++{
		resp, _ = http.Get(strings.TrimSpace(washingtmainsitemap.Locations[i]))
		bytes, _ = ioutil.ReadAll(resp.Body)
		xml.Unmarshal(bytes, &washington_news)
	}			
	resp.Body.Close()
	Page := NewsForm{ Link: washington_news.Locations, NewsPaper : "washingtonpost"}
	t, _ := template.ParseFiles("basictemplating.html")
	t.Execute(w, Page)
}

/*
Responsible for Generating SiteMaps of Ny-Times on following topics ex :
Business, Entertainment, technology, world
*/

func newyorkTimesAggregateHandler(w http.ResponseWriter, r *http.Request){

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
	Page := NewsForm{ Link: nyTimes_news.Locations, NewsPaper : "NewYorkTimes" }
	t, _ := template.ParseFiles("basictemplating.html")
	t.Execute(w, Page)

}

func main() {
	http.HandleFunc("/Home",indexHandler)
	http.HandleFunc("/washingtonpost", washingtonpostAggregateHandler)
	http.HandleFunc("/nytimes",newyorkTimesAggregateHandler)
	http.ListenAndServe(":8000", nil)
}