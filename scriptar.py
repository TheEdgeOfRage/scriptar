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

def init_db():
    return mysql.connector.connect(user='scriptar', password='vysrCuuxeJhixgBb', database='scriptar', host='localhost')

def close_db(db, cur):
    cur.close()
    db.close()


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
        db = init_db()
        cur = db.cursor()
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        cur.execute("INSERT INTO Users (username, email, password, name) VALUES (%s, %s, %s, %s, %s)", username, email, password, name)
        db.commit()
        close_db(db, cur)
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
