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
from decorators import login_required

profile_app = Blueprint('profile_app', __name__)

@profile_app.route('/')
@login_required
def profile():
    db = mysqlDB()
    query = 'SELECT sc.ID, sc.name, sc.Description, su.name FROM Scripts AS sc JOIN Subjects AS su ON su.ID=Subject_ID WHERE User_ID=%s' % session['user_id']
    db.execute(query)
    row = db.cur.fetchone()

    # script_dict = {}
    script_list = []
    current_app.logger.info(row)
    current_app.logger.info(query)

    while row is not None:
        # script_dict['id'] = str(row[0])
        # script_dict['name'] = row[1]
        # script_dict['desc'] = row[2].decode('UTF-8')
        # script_dict['subj'] = row[3]
        script_list.append({'id': str(row[0]), 'name': row[1], 'desc': row[2].decode('UTF-8'), 'subj': row[3]})
        row = db.cur.fetchone()
        current_app.logger.info(script_list)

    return render_template('profile.html', scripts=script_list)
