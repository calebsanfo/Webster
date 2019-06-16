"""
Created on Tue Jul  3 20:02:14 2018

@author: calebsanford
"""

import datetime
from pytrends.request import TrendReq
from utils import stocks_1, stocks_3, stocks_2, path, get_company_name
import sys


def google_results(curr_stock, date):
    # Login to Google. Only need to run this once, the rest of requests will use the same session.
    pytrend = TrendReq()
    weekago = date - datetime.timedelta(days=7)
    searches = pytrend.get_historical_interest([curr_stock + ' stock', curr_stock, get_company_name(curr_stock), curr_stock + ' price'],
                                               year_start=int(weekago.year),
                                               month_start=int(weekago.month),
                                               day_start=int(weekago.day),
                                               hour_start=date.today().hour,
                                               year_end=date.today().year,
                                               month_end=date.today().month,
                                               day_end=date.today().day,
                                               hour_end=date.today().hour,
                                               cat=0,
                                               geo='',
                                               gprop='',
                                               sleep=1)
    return searches

if __name__ == '__main__':
    cur_date = datetime.datetime.now()
    if sys.argv[1] == '1':
        for stock in stocks_1:
            curr_path = path + "Stock_data\Stocks" + '\\' + stock + '\\' + 'Trends' + '\\' + 'searches.csv'
            file = open(curr_path, 'a+')  # Open in append mode
            google_results(stock, cur_date).to_csv(file)
            file.close()
            print(stock + " Trends DONE!")
    elif sys.argv[1] == '2':
        for stock in stocks_2:
            curr_path = path + "Stock_data\Stocks" + '\\' + stock + '\\' + 'Trends' + '\\' + 'searches.csv'
            file = open(curr_path, 'a+')  # Open in append mode
            google_results(stock, cur_date).to_csv(file)
            file.close()
            print(stock + " Trends DONE!")
    else:
        for stock in stocks_3:
            curr_path = path + "Stock_data\Stocks" + '\\' + stock + '\\' + 'Trends' + '\\' + 'searches.csv'
            file = open(curr_path, 'a+')  # Open in append mode
            google_results(stock, cur_date).to_csv(file)
            file.close()
            print(stock + " Trends DONE!")

