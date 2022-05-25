class dataNode:
    trialNumber = 0
    Altitude = 0
    temprature = 0
    pressure = 0
    humidity = 0

    def setVals(self, trialNo, Alt, temp, pres, humid): #sets the values of the nodes
        self.trialNumber = trialNo
        self.Altitude = Alt
        self.temprature = temp
        self.pressure = pres
        self.humidity = humid

    def setAlt(self, Alt): #get and set methods for data types in the nodes
        self.Altitude = Alt

    def setTemprature(self, temprature):
        self.temprature = temprature

    def setPressure(self, pressure):
        self.pressure = pressure

    def setHumidity(self, humidity):
        self.humidity = humidity

    def setTrialNumber(self, trialNo):
        self.trialNumber = trialNo

    def gAlt(self):
        return self.Altitude

    def gTemprature(self):
        return self.temprature

    def gPressure(self):
        return self.pressure

    def gHumidity(self):
        return self.humidity

    def gTrialNumber(self):
        return self.trialNumber


