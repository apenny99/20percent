class dataNode:
    def __init__(self):
        self.trialNumber=0
        self.Altitude=0
        self.temprature=0
        self.pressure=0
        self.humidity=0


    def setVals(self,trialNo,Alt,temp,pres,humid):
        self.trialNumber=trialNo
        self.time=time
        self.temprature=temp
        self.pressure=pres
        self.humidity=humid

    def setAlt(self,Alt):
        self.Altitude=Alt

    def setTemprature(self,temp):
        self.temprature=temp

    def setPressure(self,pressure):
        self.pressure=pressure

    def setHumidity(self,humidity):
        self.humidity=humidity

    def setTrialNumber(self,trialNo):
        self.trialNumber=trialNo

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



