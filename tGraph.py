import matplotlib.pyplot as plt
import numpy as np
class tGraph:


    m=0

    def __init__(self):
        m=1


    def tvinp(self,tmpArr, ylbl,save): # method to generate graph
        end=len(tmpArr)
        i=1
        x=[]
        y=tmpArr

        while i<=end: #creates ascending array going from 1 incrementing by 1
            x.append(i)
            i+=1


        plt.plot(x,y) #plots with the arrays
        plt.xlabel('Observation no.')
        plt.ylabel(ylbl) #sets graph axis labels
        plt.title(ylbl + ' vs. Time') #sets the title
        plt.grid(True)
        if save == 'y':
            plt.savefig("test.png")#saves png of the graph
        plt.show()

