#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Filename: d:\pgala\Pedro\proyectos\immfly\immfly_api\serializers.py
# Path: d:\pgala\Pedro\proyectos\immfly\immfly_api
# Created Date: Friday, June 3rd 2022, 5:59:44 pm
# Author: Pedro Gal�n P�rez
# 
# Copyright (c) 2022 Immfly.
###

from rest_framework import serializers
from .models import Content, Channel

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'rating', 'channel', 'content_path', 'metadata']

class ChannelSerializer(serializers.ModelSerializer):

    channel_rating = serializers.SerializerMethodField('rating_mean')
    def rating_mean(self, obj):
        try:
            mean = obj.rating_mean()
            return mean
        except:
            return 0

    class Meta:
        model = Channel
        fields = ['id', 'name', 'language', 'parent', 'channel_rating', 'picture_path']
