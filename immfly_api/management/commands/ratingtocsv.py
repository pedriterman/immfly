#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Filename: d:\pgala\Pedro\proyectos\immfly\immfly_api\management\commands\ratingtocsv.py
# Path: d:\pgala\Pedro\proyectos\immfly\immfly_api\management\commands
# Created Date: Saturday, June 4th 2022, 9:12:02 am
# Author: Pedro Gal�n P�rez
# 
# Copyright (c) 2022 Immfly.
###



from django.core.management.base import BaseCommand, CommandError
from immfly_api.models import Content, Channel
import csv
import sys
import os
from immfly_api.settings import BASE_DIR

class Command(BaseCommand):
    help = ("Output all channel ordered by ratings to CSV")

    def handle(self, *args, **options):
        data = []
        channels = Channel.objects.all()
        sorted_channels = sorted(channels, reverse = True, key= lambda r: r.rating_mean())
        path = os.path.join(BASE_DIR, 'csvstorage')
        if not os.path.exists(path):
            '''
            CSV storage folder doesn't exist, make it!
            '''
            os.mkdir(path)
        model_name = "rating_sheet"
        filename = "{}.csv".format(model_name)
        filepath = os.path.join(path, filename)
        rows_done = 0
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for channel in sorted_channels:
                data.append([channel.name, channel.rating_mean()])
            writer.writerows(data)
