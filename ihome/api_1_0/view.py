# -*- coding:utf-8 -*-
from . import api


api.route("/")
def index():
    return "hello"