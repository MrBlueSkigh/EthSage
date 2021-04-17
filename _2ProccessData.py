import os
import pandas as pd
import numpy as np
from _1DataIn import DataIn

class ProccessData:
    def __init__(self):
        di = DataIn()
        prices = di.QueryAPI()
        self.CreateDataframe(prices)
    
    def CreateDataframe(self, prices):
        ethdf = pd.DataFrame(prices, columns=['Year','Month','Day','Price'])
        print(ethdf)




def __main__():
    p = ProccessData()

__main__()