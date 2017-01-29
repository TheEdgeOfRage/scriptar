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
import mysql.connector

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
mysql_con = mysql.connector.connect(user='scriptar', password='vysrCuuxeJhixgBb', database='scriptar', host='localhost')

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
        cur = mysql_con.cursor()
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        cur.execute("INSERT INTO Users (username, email, password, name) VALUES (%s, %s, %s, %s, %s)", username, email, password, name)
        mysql_con.commit()
        cur.close()
        mysql_con.close()
        return redirect(url_for('signup'))


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
        f = request.files['file']
        f.save('/srv/http/scriptar/uploads/uploaded_file.txt')
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    print(app.secret_key)
