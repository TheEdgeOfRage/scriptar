#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 pavle <pavle@hp-arch>
#
# Distributed under terms of the MIT license.

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "\xd9v\xc6\x03\x18=\xa0zn\xc8`qZ\xd0\x03}z\xb3H\x11)\xe2\x96\x0e\xfb\xa5b'\xbb5\x1f="
    MYSQL_DATABASE_USER = 'scriptar'
    MYSQL_DATABASE_PASSWORD = 'vysrCuuxeJhixgBb'
    MYSQL_DATABASE_DB = 'scriptar'
    MYSQL_DATABASE_HOST = 'localhost'


class ProductionConfig(Config):
    DEBUG = False
    FLASK_DEBUG = 0


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    FLASK_DEBUG = 1
    DEBUG = True

