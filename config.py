#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'lastflowers'
    # 该配置为True,则每次请求结束都会自动commit数据库的变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 如果设置成True(默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存,\
    # 如果不必要的可以禁用它。如果你不显示的调用它，在最新版的运行环境下，会显示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_TRACK_MODIFICATIOmigrateNS = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = '25'
    MAIL_USERNAME = 'zhaxuefeng007@163.com'
    MAIL_PASSWORD = 'cool19940928520'
    MAIL_DEFAULT_SENDER = 'lastflowers<zhaxuefeng007@163.com>'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lastflowers@127.0.0.1:3306/test'

class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lastflowers@127.0.0.1:3306/test'


config = {
    'development': DevelopmentConfig,
    'product': ProductConfig,
    'default': DevelopmentConfig
}