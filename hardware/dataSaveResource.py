# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-28 下午2:09
# File     :dataSaveResource.py.py
# Location:/Home/PycharmProjects/..
import web
import datetime
db = web.database(dbn='mysql', db='SmartHome', user='root', host='13.67.109.181', pw='root')
web.header("Access-Control-Allow-Origin", "*")


def insert_humid(humid):
    try:
        return db.insert('humid', humid=humid, time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    except IndexError:
        return None


def insert_pressure(pressure):
    try:
        return db.insert('pressure', pressure=pressure, time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    except IndexError:
        return None


def insert_temp(temp):
        try:
            return db.insert('temperature', temp=temp, time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        except IndexError:
            return None


# if __name__ == '__main__':
#
#     insert_humid(78.0)
#     insert_pressure(1.0)
#     insert_temp(21.0)
