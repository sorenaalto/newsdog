#!/usr/bin/env python3

import feedparser
import requests
from bs4 import BeautifulSoup

print("starting up!!!!")

search_string = "Baghdad+embassy"

news = feedparser.parse("https://news.google.com/rss/search?q="+search_string)


blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
	# there may be more elements you don't want, such as "style", etc.
]

for entry in news.entries:
    print(entry.link)
    print(entry.title)

    html_rsp = requests.get(entry.link)
    soup = BeautifulSoup(html_rsp.content,"html.parser")
    all_text = soup.find_all('p')
    good_text = []
    for t in all_text:
        if t.parent.name not in blacklist:
            good_text.append(t.string)

    print(good_text)

