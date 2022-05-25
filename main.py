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
    o = int(input()) #number of observations to take
    print("How long between each observation? (Seconds)")
    t = int(input()) # timing between observations
    m = cd(o, t)#creates an instance of the collectData class with the parameters
    m.startCollect() #starts the data collecting
    output = m.getArr()

    tmp = m.getDA()
    lbl = " "
    x = []
    r = tg
    print("would you like to create a graph?")

    if input() == "y": # if statement that is in charge of creating graph

        print("Would you like to save a png of the graph?(y/n)")
        save = input() #takes in what graph type is wanted
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

        r.tvinp(tg, x, lbl, save) # generates the graph with the user selected parameters

    print("Would you like to save this data to a file?(y/n)")
    if input() == "y":
        wf.simpleToFile(wf, tmp.getArr())# saves the data array to a file

    print("Would you like to take another observation? (y/n)")
    if input() == "n": #repeats the loop
        break

















    