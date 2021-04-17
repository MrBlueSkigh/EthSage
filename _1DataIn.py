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

    def __init__(self, startYear):
       self.__QueryAPI(startYear)
       
    def __QueryAPI(self, startYear):
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
        
        self.__InsertIntoDB(self.__ethPrices)

    def __InsertIntoDB(self, prices):
        # Establish DB Connection
        db = mysql.connector.connect(
            host="localhost",
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database="ethsage",
        )

        # Insert each item into the DB
        ethcursor = db.cursor()
        for e in prices:
            queryString='INSERT INTO ethprices(year,month,day,price) VALUES (%s,%s,%s,%s)'
            values=(e[0], e[1], e[2], e[3])
            ethcursor.execute(queryString, values)
            db.commit()

def __main__():
    load_dotenv()
    cc.cryptocompare._set_api_key_parameter(os.getenv('CB_API_KEY'))

    year = input("Start year: ")
    data = DataIn(int(year))

__main__()