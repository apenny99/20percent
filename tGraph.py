import matplotlib.pyplot as plt
import numpy as np
class tGraph:


    m=0

    def __init__(self):
        m=1


    def tvinp(self,tmpArr, ylbl,save):
        end=len(tmpArr)
        i=1
        x=[]
        y=tmpArr

        while i<=end:
            x.append(i)
            i+=1

        print(x)
        print(y)

        plt.plot(x,y)
        plt.xlabel('Observation no.')
        plt.ylabel(ylbl)
        plt.title(ylbl + ' vs. Time')
        plt.grid(True)
        if save == 'y':
            plt.savefig("test.png")
        plt.show()

