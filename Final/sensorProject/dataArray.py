from dataNode import dataNode as da
class dataArray:
    dataArr = []
    trialCount = 0

    def __init__(self):
        iAR = []
        iAR.append("trial No.")
        iAR.append("Altitude")
        iAR.append("Temp")
        iAR.append("Pres")
        iAR.append("Humid")
        self.dataArr.append(iAR)
    def addVal(self,dNode=da()):
        self.trialCount+=1

        smallArr = []
        smallArr.append(dNode.gTrialNumber())
        smallArr.append(dNode.gAlt())
        smallArr.append(dNode.gTemprature())
        smallArr.append(dNode.gPressure())
        smallArr.append(dNode.gHumidity())
        self.dataArr.append(smallArr)

    def printArr(self):
        for i in self.dataArr:
            print(i)
