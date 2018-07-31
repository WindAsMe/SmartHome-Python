from Adafruit_BME280 import *
import dataSaveResource
import time

# This proceeding is needed in another procedure
def read_data():
    sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    while True:

        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        hectopascals = pascals / 100
        humidity = sensor.read_humidity()

        dataSaveResource.insert_humid(humidity)
        dataSaveResource.insert_pressure(pascals)
        dataSaveResource.insert_temp(degrees)
        print ('Temp      = {0:0.3f}'.format(degrees))
        print ('Pressure  = {0:0.2f}'.format(hectopascals))
        print ('Humidity  = {0:0.2f}'.format(humidity))
        time.sleep(10)


if __name__ == '__main__':
    try:
        read_data()
    except Exception, e:
        print e
