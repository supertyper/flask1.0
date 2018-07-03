#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint

auth = Blueprint('auth',__name__,template_folder='auth_templates')

from . import views