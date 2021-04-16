import os
import requests
from dotenv import load_dotenv
import datetime
from calendar import monthrange
from collections import namedtuple
import cryptocompare as cc

def __main__():
    # Load .env file and assign API key
    load_dotenv()
    apikey = os.getenv('CB_API_KEY')

    # Init API using key
    cc.cryptocompare._set_api_key_parameter(apikey)\

    # Init variables
    day=1
    month=1
    year=2020
    eth_prices=[]
    EthSnip = namedtuple("EthSnip", ["year","month","day","price"])

    # Get historical ETH prices for every day in 2020
    for month in range(1,13):
        for day in range(1, monthrange(year,month)[1] + 1):
            price = cc.get_historical_price('ETH', 'USD', datetime.datetime(year,month,day))
            eth_prices.append(EthSnip(year,month,day,price))

    print(eth_prices)


__main__()