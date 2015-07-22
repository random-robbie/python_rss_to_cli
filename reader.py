import feedparser
d = feedparser.parse('http://www.liverpoolecho.co.uk/sport/?service=rss')
for post in d.entries:
    print post.title + ": " + post.link + "\n"
