
from utils import send_log_email
import requests
import time
import datetime
from utils import path, write_info, master_stock_list


def write_price_files(stock):
    unix_date = 0
    last_date = 0
    try:
        data = requests.get('http://www.google.com/finance/getprices?q=' + stock + '&i=60&p=6d&f=d,o,h,l,c,v').text
        # print(data)
        data_rows = data.split('\n')
        del data_rows[:7]
        # print(data_rows)
        with open(path + 'Stock_data' + '\\' + stock + '\\' + "Price_Vol" + '\\' + stock + "_data.csv", 'a+') as output:
            for rows in data_rows:
                arr = rows.split(',')
                if 'a' in arr[0]:
                    unix_date = int(arr[0][1:])
                    arr[0] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unix_date))
                else:
                    if arr[0] == '':
                        break
                    arr[0] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unix_date + (60 * int(arr[0]))))
                    last_date = arr[0]
                new_row = ','.join(arr)
                output.write(new_row)
                output.write('\n')
        write_info(stock, "Last Price: " + last_date)
        print(stock + " Price DONE!")

    except:
        print(stock+' price file write failed')
        send_log_email(stock+' price file write failed in get_price.py\nError occurred at ' + str(datetime.datetime.now()))


# Figure out how to read last date of rice and determine were to start saving
for stocks in master_stock_list:
    write_price_files(stocks)