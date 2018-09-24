#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time    : 2018/9/24 8:03 PM
# @Author  : SinTod
# @Site    : 
# @File    : settings
# @Software: PyCharm
import os

from sayhello import app

dev_db = 'sqlite:////' + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'SinTod')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
