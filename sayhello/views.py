#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time    : 2018/9/24 8:03 PM
# @Author  : SinTod
# @Site    : 
# @File    : views
# @Software: PyCharm
from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('你的信息已经发给世界~')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
