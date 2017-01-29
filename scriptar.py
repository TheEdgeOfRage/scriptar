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
from werkzeug.utils import secure_filename
from passlib.hash import argon2
import string
import random

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
        if password == request.form['password_con']:
            password = argon2.hash(password)
        name = request.form['name']
        cur.execute('INSERT INTO User (username, email, password, name, Course_ID) VALUES ("%s", "%s", "%s", "%s", %s)' % (username, email, password, name, '2', ))
        db.commit()
        close_db(db, cur)
        app.logger.debug("Sucessfully added user")
        return redirect(url_for('index'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('login'))
        else:
            return render_template('file_upload.html')
    elif request.method == 'POST':

        print(request)

        # if 'file0' not in request.files:
            # return redirect(url_for('file_upload'))

        db = init_db()
        cur = db.cursor()

        subject = request.session['subject']
        user = request.session['user']
        script_name = request.form['script_name']
        # link = request.form['link']
        description = request.form['description']
        
        file_path_base = ''.join('/srv/nginx/flask/scriptar/static/uploads/', script_name)

        for f in request.files:
            if request.files[f].filename != '' and f:
                filename = secure_filename(request.files[f].filename)
                # extension = filename.rsplit('.', 1)[1].lower()
                # filename = ''.join(['file_', 'asdf.', extension])
                file_path = ''.join([file_path_base,'/', filename])
                               
                request.files[f].save(os.path.join(file_path))
                cur.execute('INSERT INTO Scripts (name, description, Subject_ID, User_ID) VALUES ("%s", "%s", %s, %s)' % (name, description, subject, user))
        
        db.commit()
        close_db(db, cur)
        return 'kurac'


@app.route('/list_uploads')
def list_uploads():
    files = os.listdir('static/uploads/')
    return render_template('list_uploads.html', files=files)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    print(app.secret_key)
