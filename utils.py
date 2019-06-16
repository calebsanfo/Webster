"""
    General utility functions that can be used across Webster
"""


import smtplib
import requests
import os

path = r'E:' + '\\'


def send_log_email(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("<username>", "<password>")
    server.sendmail("<sender>", "<reciver>", msg)


with open('company_names.csv', 'r') as f:
    master_stock_list = [row.split(',')[0] for row in f]
    master_stock_list[0] = master_stock_list[0][3:]
    stocks_1 = master_stock_list[:639]
    stocks_2 = master_stock_list[639: 1277]
    stocks_3 = master_stock_list[1277:]


def get_company_name(symbol):
    with open('company_names.csv', 'r') as f:
        file_rows = f.read().split('\n')
        for rows in file_rows:
            row_arr = rows.split(',')
            if row_arr[0] == symbol:
                return row_arr[1]


def get_unknown_company_name_from_yahoo(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


def write_all_dirs():
    def write_directories(name):
        if not os.path.exists(path + "Stock_data" + '\\' + name):
            os.makedirs(path + "Stock_data" + '\\' + name)
            os.makedirs(path + "Stock_data" + '\\' + name + "\\" + "News")
            os.makedirs(path + "Stock_data" + '\\' + name + "\\" + "Price_Vol")
            os.makedirs(path + "Stock_data" + '\\' + name + "\\" + "StockTwits")
            os.makedirs(path + "Stock_data" + '\\' + name + "\\" + "Trends")
        if not os.path.exists(path + "Stock_data" + '\\' + name + "\\" + "info"):
            with open(path + "Stock_data" + '\\' + name + "\\" + "info.txt", "w") as output:
                output.write("Ticker: " + name + '\n')
                output.write("Company Name: " + str(get_company_name(name)) + '\n')

    print(len(master_stock_list))
    for stocks in master_stock_list:
        write_directories(stocks)

    weather_cities = [
        'NewYork',
        'Chicago',
        'London',
        'Zurich',
        'HongKong',
        'Tokyo',
        'Frankfurt',
        'Shanghai',
    ]

    for city in weather_cities:
        if not os.path.exists(path + "Weather_data" + '\\' + city):
            os.makedirs(path + "Weather_data" + '\\' + city)


def write_info(name, info):
    if not os.path.exists(path + "Stock_data" + '\\' + name + "\\" + "info"):
        with open(path + "Stock_data" + '\\' + name + "\\" + "info.txt", "a") as output:
            output.write(info + '\n')

