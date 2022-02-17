import datetime


class writeToFile:

    def simpleToFile(self, inpArr):
        minp = inpArr
        fileName = str(datetime.datetime.now())
        fileName += ".txt"
        with open(fileName, 'w') as f:
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
