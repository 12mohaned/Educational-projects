package main

import (
	"fmt"
	"html/template"
	"net/http"
)

type NewsForm struct {
	link string
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	Form := NewsForm{link: "https://www.washingtonpost.com/sitemaps/business.xml"}
	fmt.Fprintf(w, "<h1>There is nothing here but a blank page go to the news </h1>")
}

func AggregateHandler(w http.ResponseWriter, r *http.Request) {
	Form := NewsForm{link: "https://www.washingtonpost.com/sitemaps/business.xml"}
	t, error := template.ParseFiles("basictemplating.html")
	if error != nil {
		fmt.Println(error)
	}
	t.Execute(w, Form)
}

func main() {
	http.HandleFunc("/Home", indexHandler)
	http.HandleFunc("/news", AggregateHandler)
	http.ListenAndServe(":8000", nil)
	// Aggregate()
}
