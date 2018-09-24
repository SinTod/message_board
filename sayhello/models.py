#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time    : 2018/9/24 8:03 PM
# @Author  : SinTod
# @Site    : 
# @File    : models
# @Software: PyCharm
from datetime import datetime
from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
