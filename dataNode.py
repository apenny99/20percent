import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)
# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)


# "Instance Data"
timestamp = data.timestamp
temprature = data.temprature
pressure = data.pressure
humidity = data.humidity



# def newNode(time, temp, pres, humid):
#     timestamp=time
#     temprature=temp
#     pressure=pres
#     humidity=humid


# returns the timestamp
def returnTime():
    return timestamp

# returns the temprature
def returnTemp():
    return temprature

# returns the pressure
def returnPres():
    return pressure

# returns the humidity
def returnHumidity():
    return humidity


