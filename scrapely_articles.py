#!/usr/bin/python
# coding=utf-8
import html2text
import csv
from scrapely import Scraper
from urls import urls


h = html2text.HTML2Text()
s = Scraper()

# train
url1 = 'http://www.coca-colaitalia.it/storie/il-primo-ingrediente-dei-nostri-prodotti-e-lacqua'
data = {'title': 'Il primo ingrediente dei nostri prodotti è l’acqua. Ecco come lo preserviamo',
    'text': '<div id="article">',
    'author': 'Redazione Journey',
    'date': '22 mar 2017'}
s.train(url1, data)


# file opener
file_wht  = open('test.csv', "wb")
writer = csv.writer(file_wht, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow(("Titolo", "Testo", "Autore", "Data"))


# get stuff
for item in urls:
    try:
        content = s.scrape(item)[0]
        title = h.handle(content["title"][0]).encode('utf-8')
        parsed_text = h.handle(content["text"][0]).encode('utf-8')
        author = h.handle(content["author"][0]).encode('utf-8')
        date =  h.handle(content["date"][0]).encode('utf-8')

        print "Success!"
        tpl = (title, parsed_text, author, date)
        writer.writerow(tpl)
    except:
        print ":("




file_wht.close()
