from dataNode import dataNode as da


class dataArray:
    dataArr = []

    tempArr = []
    altArr = []
    presArr = []
    humArr = []

    trialCount = 0

    def __init__(self):
        iAR = []
        iAR.append("trial No.")
        iAR.append("Altitude")
        iAR.append("Temp")
        iAR.append("Pres")
        iAR.append("Humid")
        self.dataArr.append(iAR)

    def addVal(self, dNode=da()):
        self.trialCount += 1

        smallArr = []
        smallArr.append(dNode.gTrialNumber())
        smallArr.append(dNode.gAlt())
        smallArr.append(dNode.gTemprature())
        smallArr.append(dNode.gPressure())
        smallArr.append(dNode.gHumidity())

        self.tempArr.append(dNode.gTemprature())
        self.altArr.append(dNode.gAlt())
        self.presArr.append(dNode.gPressure())
        self.humArr.append(dNode.gHumidity())

        self.dataArr.append(smallArr)

    def getTempArr(self):
        return self.tempArr

    def getAltArr(self):
        return self.altArr

    def getPresArr(self):
        return self.presArr

    def getHumArr(self):
        return self.humArr




    def printArr(self):
        for i in self.dataArr:
            print(i)

    def getArr(self):
        return self.dataArr



