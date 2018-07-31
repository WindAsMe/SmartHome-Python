# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-28 下午2:33
# File     :androidResource.py
# Location:/Home/PycharmProjects/..
import web
import open_air
import open_light
import close_air
import close_light

urls = (
    '/home', 'home'
)

app = web.application(urls, globals())
web.header("Access-Control-Allow-Origin", "*")


class home:
    def GET(self, flag):
        if flag == 1:
            open_air.air_open()
            # TODO: Air on
            print("Air on")
        if flag == 2:
            close_air.air_close()
            # TODO: Air off
            print("Air off")
        if flag == 3:
            open_light.light_open()
            # TODO: Light on
            print("Light on")
        if flag == 4:
            close_light.light_close()
            # TODO: Light off
            print("Light off")


if __name__ == '__main___':
    app.run()
