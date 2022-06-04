#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Filename: d:\pgala\Pedro\proyectos\immfly\immfly_api\admin.py
# Path: d:\pgala\Pedro\proyectos\immfly\immfly_api
# Created Date: Friday, June 3rd 2022, 5:39:44 pm
# Author: Pedro Gal�n P�rez
# 
# Copyright (c) 2022 Immfly.
###


from django.contrib import  admin
from .models import Content, Channel


#Just to see the DB in django admin
admin.site.register(Content)
admin.site.register(Channel)