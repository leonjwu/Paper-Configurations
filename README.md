# Unix command to get PDFs from Google Scholar

wget -e robots=off -H --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" -r -l 1 -nd -A pdf http://scholar.google.com/scholar?q=filetype%3Apdf+statistics&btnG=&hl=en&as_sdt=0%2C23

### Search terms:
+statistical+inference
+statistics
+machine+learning
+data+science
+modelling

The papers used in this analysis can be obtained by using the search terms above and the unix command to download the raw pdfs.
