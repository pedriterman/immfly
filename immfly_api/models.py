#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Filename: d:\pgala\Pedro\proyectos\immfly\immfly_api\models.py
# Path: d:\pgala\Pedro\proyectos\immfly\immfly_api
# Created Date: Friday, June 3rd 2022, 4:51:47 pm
# Author: Pedro Gal�n P�rez
# 
# Copyright (c) 2022 Immfly.
###


from django.db import models
import statistics

class Channel(models.Model):
    #Model that defines what a channel is. It can contain another instance of Channel
    name = models.CharField(max_length=300)
    language = models.CharField(max_length=300)
    picture_path = models.CharField(max_length=300, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name = 'children')

    def __str__(self):
        return self.name + ' ' + self.language

    #METHODS

    def get_all_children(self):
        #Method to get all children of a determined Channel, including himself
        children = [self]
        try:
            child_list = self.children.all()
        except AttributeError:
            return children
        for child in child_list:
            children.extend(child.get_all_children())
        return children

    def rating_mean(self):
        #Method to get the mean of the channel and all its family tree.
        childrens = self.get_all_children()
        ratings_array = []
        for children in childrens:
            ratings = Content.objects.only('channel').filter(channel=children.id)
            if ratings:
                for rating in ratings:
                    ratings_array.append(rating.rating)
        try:
            mean = statistics.mean(ratings_array)
            return mean
        except:
            return 0

class Content(models.Model):
    #Model that defines what a content is. The metadata field can contain anything because it stores a json
    title = models.CharField(max_length=300)
    content_path = models.CharField(max_length=300, null=True, blank=True)
    rating = models.IntegerField(blank=True, null=True)
    metadata = models.JSONField(null=True)
    channel = models.ForeignKey(Channel, null=False, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + self.channel.name