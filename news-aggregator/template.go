package main
import (
	"fmt"
	"html/template"
	"encoding/xml"
	"io/ioutil"
	"net/http"
	"strings"
	"time"
)

type NewsForm struct {
	Link [] string
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

func AggregateHandler(w http.ResponseWriter, r *http.Request) {

	var mainsitemap Sitemapindex
	var news News
	var Washignton_post string = "https://www.washingtonpost.com/sitemaps/index.xml"
	resp, _ := http.Get(Washignton_post)
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &mainsitemap)
	resp.Body.Close()
	resp, _ = http.Get(strings.TrimSpace(mainsitemap.Locations[0]))
	bytes, _ = ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &news)
	resp.Body.Close()			

	Page := NewsForm{ Link: news.Locations }
	t, _ := template.ParseFiles("basictemplating.html")
	t.Execute(w, Page)

}

func main() {
	http.HandleFunc("/Home",indexHandler)
	http.HandleFunc("/news", AggregateHandler)
	http.ListenAndServe(":8000", nil)
 
}