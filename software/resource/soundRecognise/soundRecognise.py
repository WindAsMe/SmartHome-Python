# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-30 下午10:13
# File     :soundRecognise.py
# Location:/Home/PycharmProjects/..

import wave
import urllib2
import \
    pycurl
import json


# get access token by api key & secret key

def get_token():
    apiKey = "USxASXrOrk5ltfcRIjT34zCA"
    secretKey = "Maz3DjqsMsMYZ7RN3z1vwsDqZxzlHhat"
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey
    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']


def dump_res(buf):
    print buf


# post audio to server
def use_cloud(token):
    fp = wave.open('16k.wav', 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    cuid = "6a:ab:1e:7b:98:1d"  # my xiaomi phone MAC
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % f_len
    ]
    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url))  # curl doesn't support unicode
    # c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header)  # must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform()  # pycurl.perform() has no return val


if __name__ == "__main__":
    token = get_token()
    use_cloud(token)