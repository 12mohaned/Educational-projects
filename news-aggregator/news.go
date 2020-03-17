package main
import (
	"fmt"
	"encoding/xml"
	"io/ioutil"
	"net/http"
)

type Sitemapindex struct {
	Locations []string `xml:"sitemap>loc"`
}

type News struct {
	Locations []string `xml:"url>loc"`
}

type NewsMap struct {
	Keyword string
	Location string
}
func foo(){
	var s Sitemapindex
	var n News
	var Washignton_post string = "https://www.washingtonpost.com/sitemaps/index.xml"
	var Washignton_Indexes string = "https://www.washingtonpost.com/sitemaps/business.xml"
	resp, _ := http.Get(Washignton_post)
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &s)
	resp.Body.Close()
	
	resp,_ = http.Get(Washignton_Indexes)
	bytes, _ = ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &n)
	fmt.Println(n.Locations)

	resp.Body.Close()
}
