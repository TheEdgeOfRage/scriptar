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
from flask import Flask, request, session, render_template, redirect, url_for
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        if not 'user' in session:
            return render_template('signup.html')
        else:
            return redirect(url_for('index'))
    elif request.method == 'POST':
        cursor = mysql.get_db().cursor()
        username = request.form['username']
        password = request.form['password']

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('index'))
        else:
            return render_template('file_upload.html')
    elif request.method == 'POST':

        if 'file0' not in request.files:
            return redirect(url_for('file_upload'))
        
        for f in request.files:
            if request.files[f].filename != '' and f:
                filename = secure_filename(request.files[f].filename)
                request.files[f].save(os.path.join('/srv/http/scriptar/uploads', filename))
        return 'kurac'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    print(app.secret_key)
