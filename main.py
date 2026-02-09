from sources import SOURCES
from crawl import fetch_news
from filter import filter_news
from summarize import summarize
from mail import send_mail

# items = fetch_news(SOURCES)
# filtered = filter_news(items)

# if filtered:
    # send_mail(summarize(filtered))

send_mail("Bot çalıştı ama filtre boş olabilir.")
