#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 pavle <pavle@hp-arch>
#
# Distributed under terms of the MIT license.

"""

"""

from flask import Blueprint, render_template, session, current_app

from db import db as mysqlDB

profile_app = Blueprint('profile_app', __name__)

@profile_app.route('/')
def profile():
    db = mysqlDB()
    db.execute('SELECT ID, name, create_time, Description, Subject_ID FROM Scripts WHERE User_ID=%s' % session['user_id'])
    row = db.cur.fetchone()

    while row is not None:
        current_app.logger.info(row)
        row = db.cur.fetchone()

    return render_template('profile.html')
