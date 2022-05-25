# writeToFile.py
# Class that is responsible for writing the data to a file
# August Penny
# 5/2022

import datetime


class writeToFile:

    def simpleToFile(self, inpArr):
        minp = inpArr
        fileName = str(datetime.datetime.now()) #names the file as the time of the observation
        fileName += ".txt"
        with open(fileName, 'w') as f: #loop to put the data into the file
            mt = []
            while len(minp) > 0:
                mt.append(minp.pop())
            while len(mt) > 0:
                t = mt.pop()
                ts = " | "
                for a in t:
                    ts += str(a) + " | "
                ts += "\n"
                f.write(ts)
