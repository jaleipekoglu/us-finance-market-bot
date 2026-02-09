KEYWORDS = [
    "enters u.s",
    "us market",
    "expands to the u.s",
    "acquires",
    "regulatory approval",
    "banking license",
    "financial services"
    "stablecoin"
    "AI"
]

def filter_news(items):
    out = []
    for i in items:
        text = (i["title"] + " " + i["summary"]).lower()
        if any(k in text for k in KEYWORDS):
            out.append(i)
    return out

