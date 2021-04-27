import os
import matplotlib.pyplot as plt
from _1DataIn import DataIn
from _2ProccessData import ProccessData

class PlotData():
    def __init__(self):
        df = ProccessData.GetDataFromJson(self, 1)
        self.Plot(df)

    def Plot(self, df):
        plt.plot(df.columns, df.loc["Price"], 'r--')
        plt.ylabel('Price')
        plt.xlabel('Days since {day:.0f}/{month:.0f}/{year:.0f}'.format(day=df[0].Day, month=df[0].Month, year=df[0].Year))
        plt.show()


def __main__():
    plot = PlotData()

__main__()