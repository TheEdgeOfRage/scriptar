#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 pavle <pavle@hp-arch>
#
# Distributed under terms of the MIT license.

"""
Scripts for communicating with the database. Separated into a new file for accessibility between all python files
"""

import mysql.connector

class db:
    con = None
    cur = None
    def __init__(self):
        con = mysql.connector.connect(user='scriptar', password='vysrCuuxeJhixgBb', database='scriptar', host='localhost')
        cur = con.cursor()

    def callproc(procedure, data):
        return cur.callproc(procedure, data)

    def execute(query, data):
        return cur.execute(query, data)

    def close_db():
        con.commit()
        cur.close()
        con.close()

