import time

from dataNode import dataNode as dn
from dataArray import dataArray as da
import board
from adafruit_bme280 import basic as adafruit_bme280
    
class collectData:
    numberObservations=0
    secondsBetween=0
    nArr = da()
    i2c = board.I2C()
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    bme280.sea_level_pressure = 1013.25
        
    def __init__(self,numObservations,secBetween):
        self.numberObservations=numObservations
        self.secondsBetween=secBetween
    def getArr(self):
        return self.nArr
    
    def startCollect(self):
        t=1
        # bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
        # bme280.sea_level_pressure = 1013.25

        while t<=self.numberObservations:
            n=dn()
            n.setTrialNumber(t)
            n.setAlt(round(self.bme280.altitude,2))
            n.setTemprature(round(self.bme280.temperature,2))
            n.setPressure(round(self.bme280.pressure,2))
            n.setHumidity(round(self.bme280.relative_humidity,2))
            self.nArr.addVal(n)
            time.sleep(self.secondsBetween)
            t+=1
    


    
