import requests
import datetime
from utils import get_company_name, path, send_log_email, stocks_1, stocks_2, stocks_3
import sys


def get_news(ticker, days_ago):
    news_file = open(path + "Stock_data" + '\\' + ticker + '\\' + "News" + '\\' + "news_data.txt", "a+")
    company_name = str(get_company_name(ticker))
    from_date = str((datetime.datetime.now() - datetime.timedelta(days=days_ago)).isoformat())
    url = 'https://newsapi.org/v2/everything?q=' + company_name + '&from=' + from_date + '&sortBy=publishedAt&language=en&pageSize=100&apiKey=a8a235062a474764a70073a45bd9b5a0'

    r = requests.get(url)

    i = 0
    if 'articles' in r.json():
        for art in r.json().get('articles'):
            try:
                if art.get('source').get('name'):
                    news_file.write("\nSource: " + str(str(art.get('source').get('name')).encode("utf-8")))
                if art.get('title'):
                    news_file.write("\nTitle: " + str(str(art.get('title')).encode("utf-8")))
                if art.get('description'):
                    news_file.write("\nDescription: " + str(str(art.get('description')).encode("utf-8")))
                if art.get('publishedAt'):
                    news_file.write("\nPublished on: " + str(str(art.get('publishedAt')).encode("utf-8")))
                if art.get('url'):
                    news_file.write("\nURL: " + str(str(art.get('url')).encode("utf-8")))
                news_file.write("\n\n*****************************************************************\n\n")
                i = i+1
            except:
                print(ticker + "error")
                # send_log_email(ticker + "News error")
    else:
        logfile = open(path+ "logfile.txt", "a+")
        logfile.write("No articles for " + ticker)
    
    print(i)
    print(ticker + " News DONE!")
    news_file.close()


if sys.argv[1] == '1':
    for stocks in stocks_1:
        get_news(stocks, 7)
elif sys.argv[1] == '2':
    for stocks in stocks_2:
        get_news(stocks, 7)
else:
    for stocks in stocks_3:
        get_news(stocks, 7)