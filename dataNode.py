class dataNode:
    def setVals(self,trialNo,time,temp,pres,humid):
        self.trialNumber=trialNo
        self.time=time
        self.temprature=temp
        self.pressure=pres
        self.humidity=humid

    def setTime(self,time):
        self.time=time

    def setTemprature(self,temprature):
        self.temprature=temprature

    def setPressure(self,pressure):
        self.pressure=pressure

    def setHumidity(self,humidity):
        self.humidity=humidity

    def setTrialNumber(self,trialNo):
        self.trialNumber=trialNo

    def gTime(self):
        return self.time

    def gTemprature(self):
        return self.temprature

    def gPressure(self):
        return self.pressure

    def gHumidity(self):
        return self.humidity

    def gTrialNumber(self):
        return self.trialNumber



