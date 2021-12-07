
# import smbus2
# import bme280
#
# port = 1
# address = 0x76
# bus = smbus2.SMBus(port)
#
# calibration_params = bme280.load_calibration_params(bus, address)
#
#
# # the sample method will take a single reading and return a
# # compensated_reading object
# data = bme280.sample(bus, address, calibration_params)
#
# # the compensated_reading class has the following attributes
# print(data.id)
# print(data.timestamp)
# print(data.temperature)
# print(data.pressure)
# print(data.humidity)
#
# # there is a handy string representation too
from dataNode import dataNode as dn
from dataArray import dataArray as da


arr=da()
n1 = dn()
n1.setTime(1.5)
n1.setHumidity(55)
n1.setPressure(1.2)
n1.setTemprature(53)
n1.setTrialNumber(1)
n2=dn()
n2.setVals(2,34,55,8,11)

arr.addVal(n1)
arr.addVal(n2)
arr.printArr()









