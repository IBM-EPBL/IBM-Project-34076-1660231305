from datetime import date
from newsdataapi import NewsDataApiClient


def getRecentNews():
    api = NewsDataApiClient(apikey="pub_123577089f425d68a6f46636f6f725f9d5355")
    news = []
    for i in range(10):
        l = [d for d in api.news_api(country = "in",page=i,language='en')['results'] if d['pubDate'][0:10]==date.today().strftime("%Y-%m-%d")]
        news = news + l
    return news