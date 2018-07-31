# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-8-1 上午4:26
# File     :dataReceive.py
# Location:/Home/PycharmProjects/..
import MySQLdb
import open_air
import close_air
import open_light
import close_light

url = 'http://13.67.109.181:8080/man?flag='


conn = MySQLdb.connect(host='13.67.109.181',
                       user='root',
                       db='SmartHome',
                       passwd='root',
                       port=3306,
                       charset="utf8")
cursor = conn.cursor()


def get_movement():

    try:
        cursor.excute("select id, flag, is_worked from flag order by id DESC")
        id, flag, is_worked = cursor.fetchall()  # 取出cursor得到的数据
        print("id, flag, is_worked", id, flag, is_worked)
        if is_worked:
            if flag == 1:
                open_air.air_open()
            if flag == 2:
                close_air.air_close()
            if flag == 3:
                open_light.light_open()
            if flag == 4:
                close_light.light_close()
            cursor.execute("UPDATE flag SET is_worked WHERE SEX = '%d'" % id)
    except Exception, e:
        print(e)


if __name__ == '__main__':
    try:
        get_movement()
    except Exception, e:
        cursor.close()
        conn.close()  # 最后记得关闭光标和连接，防止数据泄露
