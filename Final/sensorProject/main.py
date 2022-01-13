# August Penny
# a Python class used for preliminary testing of the other classes in the sensorProject
# 12/14/2021

from collectData import collectData as cd

import time
import board
from adafruit_bme280 import basic as adafruit_bme28
u=1

while u==1:
    print("How many observations would you like to take?")
    o=int(input())
    print("How long between each observation? (Seconds)")
    t=int(input())
    m = cd(o,t)
    m.startCollect()
    output=m.getArr()
    output.printArr()
    print("Would you like to take another observation? (y/n)")
    if input() == "n":
        break
        
