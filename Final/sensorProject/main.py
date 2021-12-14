# August Penny
# a Python class used for preliminary testing of the other classes in the sensorProject
# 12/14/2021

from collectData import collectData as cd

import time
import board
from adafruit_bme280 import basic as adafruit_bme28

m = cd(5,1)

m.startCollect()

output=m.getArr()

output.printArr()
