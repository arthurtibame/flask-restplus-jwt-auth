# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: config.py
# @Date:   2018-08-18 16:55:23
# @Last Modified by:   Green
# @Last Modified time: 2018-10-15 17:44:33

import os

class Config:
    """basic config"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A0Zr98j/3yXR~XHH!jmN]LWX/,?RT'
    #SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True

    # send mail
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_ASCII_ATTACHMENTS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = '2399447849'
    MAIL_PASSWORD =  ''
    FLASKY_MAIL_SUBJECT_PREFIX = u'DevOps Flask RestPlus API'
    FLASKY_MAIL_SENDER = '2399447849@qq.com'
    FLASKY_ADMIN = '2399447849@qq.com'
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    db_host = 'localhost'
    db_user = 'root'
    db_pass = 'guo.150019'
    db_name = 'restapi'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + db_user + ':' + db_pass + '@' + db_host + '/' + db_name
    SQLALCHEMY_ECHO=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class Production(Config):
 
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': Production,
    'default': DevelopmentConfig
}

