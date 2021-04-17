import os
import pandas as pd
import numpy as np
import json
from _1DataIn import DataIn

class ProccessData:
    def __init__(self):
        di = DataIn()
        prices = di.QueryAPI()
        self.__CreateDataframe(prices)
    
    def __CreateDataframe(self, prices):
        ethdf = pd.DataFrame(prices, columns=['Year','Month','Day','Price'])
        self.__SendToJson(ethdf)

        #todo, use dataframe to train model

    def __SendToJson(self, df):
        jsonString = json.dumps(json.loads(df.to_json(orient="index")), indent=4)
        with open('EthPrices.json','x') as f:
            f.write(jsonString)

def __main__():
    p = ProccessData()

__main__()