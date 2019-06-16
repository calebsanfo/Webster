

import webhoseio
from utils import get_company_name, path, send_log_email


def get_webhose_titles(stock, APIkey):
    file = open(path + "Stock_data" + '\\' + stock + '\\' + "News" + '\\' + "news_data.txt", "a+")

    webhoseio.config(token=APIkey)
    query_params = {
        "q": "\"" + stock + " Stock\"" + "OR" + "\"" + get_company_name(stock) + "\" language:english",
        "ts": "1528944880828", # 30 days
        "sort": "relevancy"
    }
    output = webhoseio.query("filterWebContent", query_params)
    i = 0
    for arr in output["posts"]:
        if 'title' in arr:
            file.write("\nTitle: " + str(str(arr['title']).encode("utf-8")))
        if 'text' in arr:
            file.write("\nText: " + str(str(arr['text']).encode("utf-8")))
        if 'published' in arr:
            file.write("\nPublished on: " + str(str(arr['published']).encode("utf-8")))
        if arr['thread']['site']:
            file.write("\nSite: " + str(str(arr['thread']['site']).encode("utf-8")))
        file.write("\n\n*****************************************************************\n\n")
        i = i+1
    print(i)
    print(stock + "News DONE!")

    file.close()

