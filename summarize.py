def summarize(items):
    lines = []
    for i in items[:10]:
        lines.append(f"- {i['title']} ({i['source']})\n  {i['link']}")
    return "\n".join(lines)

