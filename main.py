import datetime
import matplotlib.pyplot as plt
from collectData import collectData as cd
import board
from adafruit_bme280 import basic as adafruit_bme28
from writeToFile import writeToFile as wf

import matplotlib.pyplot as plt
import numpy as np
from tGraph import tGraph as tg

from collectData import collectData as cd

import time
import board
from adafruit_bme280 import basic as adafruit_bme28

u = 1

while u == 1:
    print("How many observations would you like to take?")
    o = int(input())
    print("How long between each observation? (Seconds)")
    t = int(input())
    m = cd(o, t)
    m.startCollect()
    output = m.getArr()

    tmp = m.getDA()
    lbl = " "
    x = []
    r = tg
    print("would you like to create a graph?")

    if input() == "y":

        print("Would you like to save a png of the graph?(y/n)")
        save = input()
        print("1: Temp vs. Time   2: Pressure vs. Time   3: Humidity vs. Time   4: Altitude vs. Time")
        tmp2 = input()
        if tmp2 == "1":
            x = tmp.getTempArr()
            lbl = "Temprature"
        if tmp2 == "2":
            x = tmp.getPresArr()
            lbl = "Pressure"
        if tmp2 == "3":
            x = tmp.getHumArr()
            lbl = "Humidity"
        if tmp2 == "4":
            x = tmp.getTempArr()
            lbl = "Temprature"

        r.tvinp(tg, x, lbl, save)

    print("Would you like to save this data to a file?(y/n)")
    if input() == "y":
        wf.simpleToFile(wf, tmp.getArr())

    print("Would you like to take another observation? (y/n)")
    if input() == "n":
        break

















    