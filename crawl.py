import feedparser

def fetch_news(sources):
    items = []
    for s in sources:
        feed = feedparser.parse(s["rss"])
        for e in feed.entries:
            items.append({
                "source": s["name"],
                "title": e.title,
                "summary": e.get("summary", ""),
                "link": e.link
            })
    return items

