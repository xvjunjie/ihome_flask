# -*- coding:utf-8 -*-
from flask import Flask
from flask_wtf import CSRFProtect

from config import config_map
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session


db = SQLAlchemy()
redis_store = None



def create_app(config_name):
    app = Flask(__name__)

    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)

    # 初始化redis
    global redis_store
    redis_store = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask-session，将session数据保存到redis中
    Session(app)
    # 为flask补充csrf防护
    CSRFProtect(app)

    #这边要用的时候在导包，避免循环导包
    from ihome.api_1_0 import api
    app.register_blueprint(api, url_prefix="/api/v1.0")

    return app
