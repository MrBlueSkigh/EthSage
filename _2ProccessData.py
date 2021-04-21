import os
import pandas as pd
import numpy as np
import json
from _1DataIn import DataIn

class ProccessData:    
    def GetDataFromAPI(self):
        di = DataIn()
        prices = di.QueryAPI()
        self.__CreateDataframe(prices)
    
    def __CreateDataframe(self, prices):
        ethdf = pd.DataFrame(prices, columns=['Year','Month','Day','Price'])
        return ethdf
        #self.__SendToJson(ethdf)

        #todo, use dataframe to train model

    def __SendToJson(self, df):
        jsonString = json.dumps(json.loads(df.to_json(orient="index")), indent=4)
        with open('EthPrices.json','x') as f:
            f.write(jsonString)

    def GetDataFromJson(self, num):
        return pd.read_json('EthPrices.json')