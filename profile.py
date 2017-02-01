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
    db.execute('SELECT ID, name, Description, Subjects.name FROM Scripts JOIN Subjects ON Subjects.ID=Subject_ID WHERE User_ID=%s' % session['user_id'])
    row = db.cur.fetchone()

    script_dict = {}
    script_list = []

    while row is not None:
        # current_app.logger.info(row)
        script_dict['id'] = str(row[0])
        script_dict['name'] = row[1]
        script_dict['desc'] = row[2]
        script_dict['subj'] = row[3]
        script_list.append(script_dict)

        row = db.cur.fetchone()

    return render_template('profile.html', scripts=script_list)
