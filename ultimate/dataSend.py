# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-31 下午10:20
# File     :dataSend.py
# Location:/Home/PycharmProjects/..
import urllib
import urllib2
import time


header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
               "Content-Type": "application/json"}

url_humid = 'http://13.67.109.181:8080/h'
url_temp = 'http://13.67.109.181:8080/t'
url_press = 'http://13.67.109.181:8080/p'

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

# Database Operation
# conn=pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='weather',port=3306,charset='utf8')
# cursor = conn.cursor()
# sql = "select * from temperature_indoor"
# cursor.execute(sql)


def save_humid():
    try:
        humidity = sensor.read_humidity()
        data = {'humid': humidity}
        data_form = urllib.urlencode(data)
        req = urllib2.Request(url=url_humid, data=data_form)
        print(req)
        res = urllib2.urlopen(req)
        res = res.read()
        print(res)
    except Exception, e:
        print e


def save_temp():
    try:
        degrees = sensor.read_temperature()
        data = {'temp': degrees}
        data_form = urllib.urlencode(data)
        req = urllib2.Request(url=url_temp, data=data_form)
        res = urllib2.urlopen(req)
        res = res.read()
        print(res)
    except Exception, e:
        print e


def save_press():
    try:
        pascals = sensor.read_pressure()
        hectopascals = pascals / 100
        data = {'press': hectopascals}
        data_form = urllib.urlencode(data)
        req = urllib2.Request(url=url_press, data=data_form)
        res = urllib2.urlopen(req)
        res = res.read()
        print(res)
    except Exception, e:
        print e


if __name__ == '__main__':
    try:
        while True:
            save_humid()
            save_press()
            save_temp()
            time.sleep(10)
    except Exception, e:
        print(e.message)
