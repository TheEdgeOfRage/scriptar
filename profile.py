#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 pavle <pavle@hp-arch>
#
# Distributed under terms of the MIT license.

"""

"""

from flask import Blueprint, render_template

profile_app = Blueprint('profile_app', __name__)

@profile_app.route('/')
def profile():
    return render_template('profile.html')
