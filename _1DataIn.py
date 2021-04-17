import os
import requests
from dotenv import load_dotenv
import datetime
from calendar import monthrange
from collections import namedtuple
import mysql.connector
import cryptocompare as cc

class DataIn:
    __ethPrices = []

    def __init__(self):
       load_dotenv()
       cc.cryptocompare._set_api_key_parameter(os.getenv('CB_API_KEY'))
       
    def QueryAPI(self):
        startYear = input("Start Year: ")
        startYear = int(startYear)
        EthSnip = namedtuple("EthSnip", ["year","month","day","price"])
        # Get historical ETH prices from start year to end of last full year
        for year in range(startYear, datetime.date.today().year):
            for month in range(1,13):
                for day in range(1, monthrange(startYear,month)[1] + 1):
                    price = cc.get_historical_price('ETH', 'USD', datetime.datetime(year,month,day))
                    self.__ethPrices.append(EthSnip(year,month,day,price['ETH']['USD']))
                print("Aquired prices for " + str(month) + "/" + str(year))
            print("Aquired prices for " + str(year))

        # Get historical ETH prices from beginning of current year to last full month
        year = datetime.date.today().year   
        for month in range(1,datetime.date.today().month):
            for day in range(1, monthrange(year,month)[1] + 1):
                price = cc.get_historical_price('ETH', 'USD', datetime.datetime(year,month,day))
                self.__ethPrices.append(EthSnip(year,month,day,price['ETH']['USD']))
            print("Aquired prices for " + str(month) + "/" + str(year))

        # Get historical ETH prices of the current month up to the current day
        startMonth = datetime.date.today().month
        for day in range(1, datetime.date.today().day):
            price = cc.get_historical_price('ETH', 'USD', datetime.datetime(year,month,day))
            self.__ethPrices.append(EthSnip(year,month,day,price['ETH']['USD']))
        
        # Return List
        return self.__ethPrices