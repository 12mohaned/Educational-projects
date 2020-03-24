package main
import (
	"encoding/xml"
	"io/ioutil"
	"net/http"
	"strings"
)

func MainSiteMap(){
	var mainsitemap Sitemapindex
	var news News
	var Washignton_post string = "https://www.washingtonpost.com/sitemaps/index.xml"

	resp, _ := http.Get(Washignton_post)
	bytes, _ := ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &mainsitemap)
	resp.Body.Close()
	
	for i:=0; i < 1;i++{
	resp, _ = http.Get(strings.TrimSpace(mainsitemap.Locations[i]))
	bytes, _ = ioutil.ReadAll(resp.Body)
	xml.Unmarshal(bytes, &news)
	resp.Body.Close()
}

}
//{ business-sitemap }
//{article1, article2, article 3, article 4 }