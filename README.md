# How to fetch PDFs from Google Scholar

The papers used can be acquired using the following unix command:

```
wget -e robots=off -H --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 #Firefox/3.0.3" -r -l 1 -nd -A pdf http://scholar.google.com/scholar?q=filetype%3Apdf+statistics&btnG=&hl=en&as_sdt=0%2C23
```

#### The search terms that I used were:
- +statistical+inference
- +statistics
- +machine+learning
- +data+science
- +optimization
- +modelling
- +statistical+learning
- +machine+learning
