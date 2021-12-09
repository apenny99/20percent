import time

from dataNode import dataNode as dn
from dataArray import dataArray as da
from Adafruit_BME280 import *

class collectData:
    numberObservations=0
    secondsBetween=0
    nArr = da()
    # sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8 )

    def __init__(self,numObservations,secBetween):
        self.numberObservations=numObservations
        self.secondsBetween=secBetween

    def startCollect(self):
        t=1

        while t<=self.numberObservations:
            tme=t*self.numberObservations
            tN=dn()
            tN.setTrialNumber(t)
            tN.setTime(tme)
            # tN.setTemprature(sensor.read_temprature())
            # tN.setPressure(sensor.read_pressure)
            # tN.setHumidity(sensor.read_humidity())
            time.sleep(self.secondsBetween)
            t+=1
    def getDaA(self):
        return self.nArr()