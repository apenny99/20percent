import dataNode
class dataArray:

    bigarr = [["Data Point No. ","Time", "Temprature", "Pressure", "Humidity"]]
    nodeArr = []
    bigArrLength=0
    nodeArrLength=0


# array containing the values from each trial
    def addVal(self,time, temp, pres, humid,counter):
        smallArr = [counter, time, temp, pres, humid] # make int counter that increments every time a data node is added
        dataArray.bigarr.append(smallArr)
        dataArray.bigArrLength+=1




# array containing each consecutive node
    def addNode(self,dataPoint):
        dataArray.nodeArr.append(dataPoint)
        dataArray.nodeArrLength+=1



# prints out the values of the array
    def printArray(self):
        for i in dataArray.bigarr:
            print(i)







