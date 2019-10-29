# -*- coding: UTF-8 -*-
import base64
from db import DataBaseClient
from read_config import ConfigReader


mysql_config = ConfigReader().get("default")


def url_decode(url_64):
    return base64.b64decode(url_64)


def url_encode(url):
    return base64.b64encode(url)


def get_v2ray(token, response, shared=False):
    db = DataBaseClient(**mysql_config)
    db.connection()
    if shared:
        user = db.execute("SELECT user FROM token WHERE token = '{} '".format(token))[0][0]
    else:
        user = "shared"
    v2rays = db.execute("SELECT url FROM v2ray WHERE user = '{}'".format(user))
    for v2ray in v2rays:
        response["v2ray"] += (v2ray[0] + "\n")
    db.close()


def get_ss(token, response, shared=False):
    db = DataBaseClient(**mysql_config)
    db.connection()
    if shared:
        user = db.execute("SELECT user FROM token WHERE token = '{} '".format(token))[0][0]
    else:
        user = "shared"
    v2rays = db.execute("SELECT url FROM ss WHERE user = '{}'".format(user))
    for v2ray in v2rays:
        response["ss"] += (v2ray[0] + "\n")
    db.close()


def get_admin_not_shared():
    db = DataBaseClient(**mysql_config)
    db.connection()
    v2rays = db.execute("SELECT url FROM v2ray WHERE is_shared = 0 and user = 'admin'")
    sss = db.execute("SELECT url FROM ss WHERE is_shared = 0 and user = 'admin'")
    v = ""
    s = ""
    for v2ray in v2rays:
        v += (v2ray[0] + "\n")
    for ss in sss:
        s += (ss[0] + "\n")
    db.close()
    return "{}\n{}".format(s, v)


def is_admin(token):
    db = DataBaseClient(**mysql_config)
    db.connection()
    try:
        user = db.execute("SELECT user FROM token WHERE token = '{} '".format(token))[0][0]
    except IndexError:
        return False
    if user == "admin":
        return True
    else:
        return False


if __name__ == '__main__':
    pass
