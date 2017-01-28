#! env/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 pavle <pavle@hp-arch>
#
# Distributed under terms of the MIT license.

"""

"""

import os
from flask import Flask, request, session, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method() == 'GET':
        if session['user'] == None:
            return render_template('signup.html')
        else:
            return redirect(url_for('index'))
    elif request.method() == 'POST':
        username = request.form['username']
        password = request.form['password']

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    print(app.secret_key)
