# August Penny
# A python class that takes in dataNode objects and puts them in the format of a 2d array
# to store the data and make it accessible later.
# 12/14/2021

from dataNode import dataNode as da
class dataArray:
    dataArr = []
    trialCount = 0

    def __init__(self): # makes first row of the array the labels for the columns
        iAR = []
        iAR.append("| trial No. ")
        iAR.append("| Altitude ")
        iAR.append("| Temp ")
        iAR.append("| Pres ")
        iAR.append("| Humid |")
        self.dataArr.append(iAR)

    def addVal(self,dNode=da()): # adds the values of a node to a small array then puts small array on the big array
        self.trialCount+=1

        smallArr = []
        smallArr.append(dNode.gTrialNumber())
        smallArr.append(dNode.gAlt())
        smallArr.append(dNode.gTemprature())
        smallArr.append(dNode.gPressure())
        smallArr.append(dNode.gHumidity())
        self.dataArr.append(smallArr)

    def printArr(self): # prints out the array
        for i in self.dataArr:
            print(i)
