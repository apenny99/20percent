import time
# import smbus2
# import bme280
from dataNode import dataNode as dn
from dataArray import dataArray as da
# port = 1
# address = 0x76
# bus = smbus2.SMBus(port)
#
# calibration_params = bme280.load_calibration_params(bus, address)
#
#
# # the sample method will take a single reading and return a
# # compensated_reading object
# data = bme280.sample(bus, address, calibration_params)

class collectData:
    numberObservations=0
    secondsBetween=0
    t2 = da()
    def __init__(self,numObservations,secBetween):
        self.numberObservations=numObservations
        self.secondsBetween=secBetween

    def startCollect(self):
        t=1

        while t<=self.numberObservations:

            temp = dn()
            temp.setTrialNumber(t)
            temp.setTime(t*self.secondsBetween)
            temp.setTemprature(1)
            temp.setPressure(1)
            temp.setHumidity(1)
            # temp.setTemprature(data.temprature)
            # temp.setPressure(data.pressure)
            # temp.setHumidity(data.humidity)
            self.t2.addVal(temp)
            

            time.sleep(self.secondsBetween)
            t+=1
    def getDaA(self):
        return self.t2