import os
import coinbase as cb
import requests
from dotenv import load_dotenv

def __main__():
    load_dotenv()
    apikey = os.getenv('CB_API_KEY')
    apisecret = os.getenv('CB_API_SECRET')
    coinbase = cb.Coinbase.with_api_key(apikey, apisecret)
    #user = coinbase.get_user()
    #print(user["name"])
    #balance = coinbase.get_balance()
    #print("Balance: " + balance)

__main__()