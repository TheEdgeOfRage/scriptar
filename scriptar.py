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
from flask import Flask, request, session, render_template, redirect, url_for, flash
import mysql.connector
from werkzeug.utils import secure_filename
from passlib.hash import argon2
import string
import random

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

def init_db():
    con = mysql.connector.connect(user='scriptar', password='vysrCuuxeJhixgBb', database='scriptar', host='localhost')
    return (con, con.cursor())

def close_db(db, cur):
    cur.close()
    db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        if not 'user_id' in session:
            return render_template('signup.html')
        else:
            return redirect(url_for('index'))
    elif request.method == 'POST':
        (db, cur) = init_db()

        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        name = request.form['name'].strip()

        if password == request.form['password_con'].strip():
            password = argon2.hash(password)
        else:
            flash('Passwords do not match', 'error')
            close_db(db, cur)
            return render_template('signup.html', username=username, email=email, name=name)

        cur.callproc('createUser', (username, email, password, name))
        data = cur.stored_results()
        result = None
        for item in data:
            result = item
            break

        if result:
            close_db(db, cur)
            app.logger.debug(result.fetchall())
            # flash(result.fetchall(), 'error')
            return render_template('signup.html', username=username, email=email, name=name)

        db.commit()
        close_db(db, cur)
        return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if not 'user_id' in session:
            return render_template('login.html')
        else:
            return redirect(url_for('index'))
    elif request.method == 'POST':
        (db, cur) = init_db()
        username = request.form['username']
        password = request.form['password']
        cur.execute('SELECT ID, password from Users WHERE username="%s"', (username,))
        for (user_id, password_db) in cur:
            print(password_db)
            if argon2.verify(password, password_db):
                session['user_id'] = user_id
                return redirect(url_for('index'))
            else:
                return redirect(url_for('login'))
        return redirect(url_for('signup'))


@app.route('/logout')
def logout():
    if not 'user_id' in session:
        return redirect(url_for('login'))
    else:
        session.pop('user_id', None)
        return redirect(url_for('index'))


@app.route('/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'GET':
        if 'user_id' not in session:
            return redirect(url_for('login'))
        else:
            return render_template('file_upload.html')
    elif request.method == 'POST':
        (db, cur) = init_db()

        # subject = request.form['subject']
        user_id = session['user_id']
        subject = '1'
        script_name = request.form['script_name']
        description = request.form['description']
        # link = request.form['link']

        file_path_base = ''.join(['/srv/http/scriptar/static/uploads/', script_name])
        os.makedirs(file_path_base, mode=0o775, exist_ok=True)

        print(request.files)
        for f in request.files:
            if request.files[f].filename != '' and f:
                filename = secure_filename(request.files[f].filename)
                # extension = filename.rsplit('.', 1)[1].lower()
                # filename = ''.join(['file_', 'asdf.', extension])
                file_path = ''.join([file_path_base,'/', filename])

                request.files[f].save(os.path.join(file_path))
                cur.execute('INSERT INTO Scripts (name, description, Subject_ID, User_ID) VALUES ("%s", "%s", %s, %s)', (script_name, description, subject, user_id))

        db.commit()
        close_db(db, cur)
        return 'Upload sucessful'


@app.route('/list_uploads')
def list_upload_dirs():
    dirs = os.listdir('static/uploads/')
    return render_template('list_upload_dirs.html', dirs=dirs)


@app.route('/list_uploads/<script_name>')
def list_uploads(script_name):
    files = os.listdir('static/uploads/%s/' % script_name)
    return render_template('list_uploads.html', files=files, name=script_name)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    print(app.secret_key)
