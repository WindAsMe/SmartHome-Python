# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-28 下午2:09
# File     :hello.py.py
# Location:/Home/PycharmProjects/..
import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())


class hello:

    def GET(self, name):
        return open(r'hello.html', 'r').read()


if __name__ == '__main__':
    app.run()
