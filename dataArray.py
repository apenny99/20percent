from dataNode import dataNode as da
class dataArray:
    dataArr = []


    def addVal(self,dNode=da()):
        self.dataArr.append(dNode)
    def printArr(self):
        for i in self.dataArr:
            print(i.gTime)









