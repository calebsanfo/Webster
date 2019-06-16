"""
Created on Tue Jul  3 21:15:14 2018

@author: calebsanford
"""

from weather import Weather, Unit
import datetime
from utils import send_log_email
import csv


def get_weather_data(id):
    try:
        weather = Weather(unit=Unit.FAHRENHEIT)
        location = weather.lookup(id)  # lookup by woeid
        condition = location.condition
        curr_temp = condition.temp
        wind_speed = location.wind.speed
        forecasts = location.forecast
        city = location.title
        city = city.replace("Yahoo! Weather - ", "")
        return [str(datetime.datetime.now()), city, curr_temp, condition.text, wind_speed,
                "1 Days out", forecasts[1].text, forecasts[1].high, forecasts[1].low, forecasts[1].code,
                "2 Days out", forecasts[2].text, forecasts[2].high, forecasts[2].low, forecasts[2].code,
                "3 Days out", forecasts[3].text, forecasts[3].high, forecasts[3].low, forecasts[3].code,
                "4 Days out", forecasts[4].text, forecasts[4].high, forecasts[4].low, forecasts[4].code,
                "5 Days out", forecasts[5].text, forecasts[5].high, forecasts[5].low, forecasts[5].code]
    except:
        print(str(id) + "Error getting weather")
        send_log_email(str(id) + "Error getting weather\nError occurred at " + str(datetime.datetime.now()))


weather_cities = [
    2459115, #'New York',
    2379574, #'Chicago',
    44418, #'London, UK',
    784794, #'Zurich, Switzerland',
    2165352, #'Hong Kong',
    1118370, #'Tokyo',
    650272, #'Frankfurt, Germany',
    2151849, #'Shanghai',
]


def write_to_csv(data, path):
    try:
        with open(path, "a+") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow(data)
    except:
        send_log_email("could not write csv weather file on: \n" + str(datetime.datetime.now()))

if __name__ == '__main__':
        write_to_csv(get_weather_data(weather_cities[0]), r"Weather_data\NewYork\data.csv")
        write_to_csv(get_weather_data(weather_cities[1]), r"Weather_data\Chicago\data.csv")
        write_to_csv(get_weather_data(weather_cities[2]), r"Weather_data\London\data.csv")
        write_to_csv(get_weather_data(weather_cities[3]), r"Weather_data\Zurich\data.csv")
        write_to_csv(get_weather_data(weather_cities[4]), r"Weather_data\HongKong\data.csv")
        write_to_csv(get_weather_data(weather_cities[5]), r"Weather_data\Tokyo\data.csv")
        write_to_csv(get_weather_data(weather_cities[6]), r"Weather_data\Frankfurt\data.csv")
        write_to_csv(get_weather_data(weather_cities[7]), r"Weather_data\Shanghai\data.csv")
