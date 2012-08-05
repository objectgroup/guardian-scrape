#!/usr/bin/python
 
import urllib
import json

def retrieve(page_number, key):
    urllib.urlretrieve("http://content.guardianapis.com/search?from-date=2011-07-01&to-date=2012-07-01&page={0}&page-size=50&format=json&show-fields=all&show-tags=all&api-key={1}".format(page_number, key), "output/guardian_page{0}.json".format(page_number))
    print page_number

key = raw_input("Enter key: ")

retrieve(1, key)

with open('output/guardian_page1.json', 'r') as f:
    output = json.load(f)
    pages = output['response']['pages']

for i in range(2, pages + 1):
    retrieve(i, key)
