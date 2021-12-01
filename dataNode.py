# import smbus2
# import bme280

# port = 1
# address = 0x76
# bus = smbus2.SMBus(port)
#
# calibration_params = bme280.load_calibration_params(bus, address)
# # the sample method will take a single reading and return a
# # compensated_reading object
# data = bme280.sample(bus, address, calibration_params)


# "Instance Data"
# timestamp = data.timestamp
# temprature = data.temprature
# pressure = data.pressure
# humidity = data.humidity

class dataNode:
    timestamp = 0
    temprature = 0
    pressure = 0
    humidity = 0



    def newNode(self, time, temp, pres, humid):
        timestamp=time
        temprature=temp
        pressure=pres
        humidity=humid


# returns the timestamp
    def getTime(self):
        return dataNode.timestamp

# returns the temprature
    def getTemp(self):
        return dataNode.timestamp

# returns the pressure
    def getPres(self):
        return dataNode.pressure

# returns the humidity
    def getHumidity(self):
        return dataNode.humidity


