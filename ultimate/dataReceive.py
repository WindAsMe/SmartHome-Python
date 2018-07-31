# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-8-1 上午4:26
# File     :dataReceive.py
# Location:/Home/PycharmProjects/..
import urllib2

import open_air
import close_air
import open_light
import close_light

url = 'http://13.67.109.181:8080/work'


def get_movement():

    try:
        req = urllib2.Request(url=url)
        print(req)
        res = urllib2.urlopen(req)
        res = res.read()
        if res["data"]["is_worked"]:
            if res["data"]["flag"] == 1:
                open_air.air_open()
            if res["data"]["flag"] == 2:
                close_air.air_close()
            if res["data"]["flag"] == 3:
                open_light.light_open()
            if res["data"]["flag"] == 4:
                close_light.light_close()
    except Exception, e:
        print(e)


if __name__ == '__main__':
    try:
        get_movement()
    except Exception, e:
        print(e.message)
