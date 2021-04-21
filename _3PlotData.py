import os
import matplotlib.pyplot as plt
from _1DataIn import DataIn
from _2ProccessData import ProccessData

class PlotData():
    def __init__(self):
        df = ProccessData.GetDataFromJson(self, 1)
        self.TestPlot(df)
        
    def __CreatePlot(self, df, height_multiplier, min_val, max_val):
        image_width = len(df)
        image_height = height_multiplier*image_width
        image = np.zeros((image_height, image_width))
        factor = image_height/(max_val-min_val)
        plt.plot()

    def TestPlot(self, df):
        start = 1
        timestep = 50
        window = int(timestep*1)
        max_val = df[start-window:start+timestep].max()
        min_val = df[start-window:start+timestep].min()
        #image = self.__CreatePlot(data[start:start+timestep], 1, min_val, max_val)
        plt.plot(df, df, 'r--')
        plt.show()


def __main__():
    plot = PlotData()

__main__()