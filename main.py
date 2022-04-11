import matplotlib.pyplot as plt
import numpy as np


from collectData import collectData as cd

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
    print("Would you like to view a graph of your results?(y/n)")
    if input() == "y":


    print("Would you like to take another observation? (y/n)")
    if input() == "n":
        break

