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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if not 'user' in session:
            return render_template('login.html')
        else:
            return redirect(url_for('index'))
    elif request.method == 'POST':
        db = init_db()
        cur = db.cursor()
        username = request.form['username']
        password = request.form['password']
        cur.execute('SELECT password from User WHERE username="%s"' % (username,))
        for (password_db,) in cur:
            print(password_db)
            if argon2.verify(password, password_db):
                session['user'] = username
                return redirect(url_for('index'))
            else:
                return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if not 'user' in session:
        return redirect(url_for('login'))
    else:
        session.pop('user', None)
        return redirect(url_for('index'))


@app.route('/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'GET':
        if 'user' not in session:
            return redirect(url_for('login'))
        else:
            return render_template('file_upload.html')
    elif request.method == 'POST':

        # if 'file0' not in request.files:
            # return redirect(url_for('file_upload'))

        db = init_db()
        cur = db.cursor()

        # subject = request.form['subject']
        # user = session['user']
        subject = '1'
        user = '6'
        script_name = request.form['script_name']
        description = request.form['description']
        # link = request.form['link']

        file_path_base = ''.join(['/srv/http/scriptar/static/uploads/', script_name])
        os.makedirs(file_path_base, mode=0o775, exist_ok=True)

        for f in request.files:
            if request.files[f].filename != '' and f:
                filename = secure_filename(request.files[f].filename)
                # extension = filename.rsplit('.', 1)[1].lower()
                # filename = ''.join(['file_', 'asdf.', extension])
                file_path = ''.join([file_path_base,'/', filename])

                request.files[f].save(os.path.join(file_path))
                cur.execute('INSERT INTO Script (name, description, Subject_ID, User_ID) VALUES ("%s", "%s", %s, %s)' % (script_name, description, subject, user))

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
