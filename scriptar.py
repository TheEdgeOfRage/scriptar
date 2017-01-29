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
        # uploaded_files = request.files['file']
        # for file in uploaded_files:
        #     file.save('/srv/http/scriptar/uploads/uploaded_file.txt')
        # return redirect(url_for('index'))

        # check if the post request has the file part
        if 'file' not in request.files:
            # flash('No file part')
            return redirect(url_for('file_upload'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            # flash('No selected file')
            return redirect(url_for('file_upload'))
        if file: #and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join('/srv/http/scriptar/uploads/', filename))
            # return redirect(url_for('uploaded_file', filename=filename))
            return 'kurac'





if __name__ == "__main__":
    app.run(host='0.0.0.0')
    print(app.secret_key)
