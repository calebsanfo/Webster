
import requests


def get_stocktwits_sentiment(stock):
    r = requests.get('https://api.stocktwits.com/api/2/streams/symbol/'+stock+'.json')
    basic_array = []
    for ent in r.json().get('messages'):
        if isinstance(ent.get('entities').get('sentiment'), dict):
            if 'basic' in ent.get('entities').get('sentiment').keys():
                basic_array.append((ent.get('entities').get('sentiment').get('basic')))
    return basic_array, len(r.json().get('messages'))

