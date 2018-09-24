#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time    : 2018/9/24 8:02 PM
# @Author  : SinTod
# @Site    : 
# @File    : errors
# @Software: PyCharm
from flask import render_template

from sayhello import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500