# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-28 下午2:33
# File     :androidResource.py
# Location:/Home/PycharmProjects/..
import web

urls = (
    '/home', 'home'
)

app = web.application(urls, globals())


class home:
    def GET(self, flag):
        if flag == 1:
            # TODO: Air on
            print("Air on")
        if flag == 2:
            # TODO: Air off
            print("Air off")
        if flag == 3:
            # TODO: Light on
            print("Light on")
        if flag == 4:
            # TODO: Light off
            print("Light off")
