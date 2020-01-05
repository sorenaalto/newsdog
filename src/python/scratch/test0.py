#!/usr/bin/env python3

import feedparser
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer

class Article:
    def __init__(self,url,title,text):
        self.url = url
        self.title = title
        self.data = text


print("starting up!!!!")

search_string = "Baghdad+embassy"

check_load = requests.get("https://news.google.com/rss/search?q="+search_string)
print("check_load",check_load)

#news = feedparser.parse("https://news.google.com/rss/search?q="+search_string)
news = feedparser.parse(check_load.text)

print("news=",news)

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

articles = []

for entry in news.entries[0:10]:
    print(entry.link)
    print(entry.title)

    html_rsp = requests.get(entry.link)
    soup = BeautifulSoup(html_rsp.content,"html.parser")
    all_text = soup.find_all('p')
    good_text = []
    for t in all_text:
        # probably don't need this check anymore...
        if t.parent.name not in blacklist:
            if t.string != None:
                good_text.append(t.string)

    print(good_text)

    articles.append(Article(entry.link,entry.title,good_text))

vectorizer = TfidfVectorizer(max_df=0.5, max_features=25,
                            min_df=2, stop_words='english',
                            use_idf=True)

X = vectorizer.fit_transform([" ".join(x.data) for x in articles])
print("X=",X)