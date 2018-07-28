# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-28 下午2:09
# File     :dataSaveResource.py.py
# Location:/Home/PycharmProjects/..
import web

db = web.database(dbn='mysql', db='SmartHome', user='root', pw='change123')


def insert_humid(humid):
    try:
        return db.insert('humid', humid=humid)
    except IndexError:
        return None


def insert_pressure(pressure):
    try:
        return db.insert('pressure', pressure=pressure)
    except IndexError:
        return None


def insert_temp(temp):
        try:
            return db.insert('temperature', temp=temp)
        except IndexError:
            return None

