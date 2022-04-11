import matplotlib.pyplot as plt
import numpy as np
class tGraph:


    def tvinp(self, tmpArr, ylbl,save):
        end=tmpArr.length
        i=0
        x=[]
        y=tmpArr

        while i<end:
            x.append(i)
            i+=1



        plt.plot(x,y)
        plt.xlabel('Observation no.')
        plt.ylabel(ylbl)
        plt.title(ylbl + ' vs. Time')
        plt.grid(True)
        if save == 'y':
            plt.savefig("test.png")
        plt.show()

