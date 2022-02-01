# from collectData import collectData as cd
#
import datetime
from time import *
# import board
# from adafruit_bme280 import basic as adafruit_bme28








m=[[5,5,6,3,5,7,8],[3,3,3,3],[4,6,7,8,7]]









fileName = str(datetime.datetime.now())
with open(fileName, 'w') as f:
    mt=[]
    while len(m)>0:
        mt.append(m.pop())
    while len(mt) > 0:
        t = mt.pop()
        ts = " | "
        for a in t:
            ts += str(a) + " | "
        ts+="\n"
        f.write(ts)






