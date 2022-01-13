# August Penny
# A Python class that creates a node object that can hold five values of data and can be
# referenced later on in other code
# 12/14/21

class dataNode:
    trialNumber=0
    Altitude=0
    temprature=0
    pressure=0
    humidity=0
    
    def setVals(self,trialNo,Alt,temp,pres,humid): # method to set all values at same time
        self.trialNumber=trialNo
        self.Altitude=Alt
        self.temprature=temp
        self.pressure=pres
        self.humidity=humid

    def setAlt(self,Alt): # method to set altitude
        self.Altitude=Alt

    def setTemprature(self,temprature): # method to set temp
        self.temprature=temprature

    def setPressure(self,pressure): # method to set pressure
        self.pressure=pressure

    def setHumidity(self,humidity): # method to set humidity
        self.humidity=humidity

    def setTrialNumber(self,trialNo): # method to set trial number
        self.trialNumber=trialNo

    def gAlt(self): # method to get altitude
        return self.Altitude

    def gTemprature(self): # method to get temp
        return self.temprature

    def gPressure(self): # method to get pressure
        return self.pressure

    def gHumidity(self): # method to get humidity
        return self.humidity

    def gTrialNumber(self): # method to get trial number
        return self.trialNumber

