#!/usr/bin/env python3

import feedparser

print("starting up!!!!")

search_string = "Baghdad+embassy"

news = feedparser.parse("https://news.google.com/rss/search?q="+search_string)

for entry in news.entries:
    print(entry.summary)
