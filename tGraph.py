import matplotlib.pyplot as plt
import numpy as np
class tGraph:

    def __init__(self):


    def tvtmp(self, arr, strt, end, save):
        tmp1=strt
        while  tmp1<end:


        plt.plot(x,y)
        plt.xlabel('Observation no.')
        plt.ylabel('Temprature (C)')
        plt.title('Temorature over time')
        plt.grid(True)
        if save == 'y':
            plt.savefig("test.png")
        plt.show()

