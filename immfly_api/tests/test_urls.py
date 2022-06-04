#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Filename: d:\pgala\Pedro\proyectos\immfly\immfly_api\tests\test_urls.py
# Path: d:\pgala\Pedro\proyectos\immfly\immfly_api\tests
# Created Date: Saturday, June 4th 2022, 11:31:48 am
# Author: Pedro Gal�n P�rez
# 
# Copyright (c) 2022 Immfly.
###

from asyncio.windows_events import NULL

from immfly_api.models import Content, Channel

from django.test import TestCase

class JSONViewTestCase(TestCase):
    def setUp(self):
        #Fill the test database with some contents and channels
        Channel.objects.create(name="TV SHOWS", language="SPANISH", parent=None, picture_path="/media/tv.jpg")
        Channel.objects.create(name="HISTORICAL", language="SPANISH", parent_id=1, picture_path="/media/hist.jpg")
        Channel.objects.create(name="WORLD WAR 1", language="SPANISH", parent_id=2, picture_path="/media/war1.jpg")
        Channel.objects.create(name="WORLD WAR 2", language="SPANISH", parent_id=2, picture_path="/media/war2.jpg")

        Content.objects.create(title="VIKINGS", rating="8", channel_id=2, content_path="/media/vikings1.mp4", metadata={"decripcion": "los vikings", "director": "Un señor"})
        Content.objects.create(title="LOS TUDOR", rating="5", channel_id=2, content_path="/media/tudor1.mp4", metadata={"año": "20XX", "director": "Un señor", "capitulos": "12"})
        Content.objects.create(title="CHERNBOBYL", rating="9", channel_id=2, content_path="/media/chernobyl1.mp4", metadata={"año": "20XX", "director": "Otro señor", "capitulos": "12"})
        Content.objects.create(title="SOÑANDO SOÑANDO TRIUNFÉ AMETRALLANDO", rating="7", channel_id=3, content_path="/media/dream.mp4", metadata={"Idiomas": "7", "director": "Un señor", "capitulos": "12"})
        Content.objects.create(title="NAZI SCHOOL MUSICAL", rating="6", channel_id=3, content_path="/media/school.mp4", metadata={"subtitulos": "Si", "director": "Un señor", "capitulos": "12"})

    def test_channel_list(self):
        #Testing if API shows all Channels
        response = self.client.get('/channels/')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'id': 1, 'name': 'TV SHOWS', 'language': 'SPANISH', 'parent': None, 'channel_rating': 7, 'picture_path': '/media/tv.jpg'},
            {'id': 2, 'name': 'HISTORICAL', 'language': 'SPANISH', 'parent': 1, 'channel_rating': 7, 'picture_path': '/media/hist.jpg'},
            {'id': 3, 'name': 'WORLD WAR 1', 'language': 'SPANISH', 'parent': 2, 'channel_rating': 6.5, 'picture_path': '/media/war1.jpg'},
            {'id': 4, 'name': 'WORLD WAR 2', 'language': 'SPANISH', 'parent': 2, 'channel_rating': 0, 'picture_path': '/media/war2.jpg'}]
        )

    def test_content_list(self):
        #Testing if API shows all contents
        response = self.client.get('/contents/')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'id': 1, 'title': 'VIKINGS', 'rating': 8, 'channel': 2, 'content_path': '/media/vikings1.mp4', 'metadata': {'decripcion': 'los vikings', 'director': 'Un señor'}},
            {'id': 2, 'title': 'LOS TUDOR', 'rating': 5, 'channel': 2, 'content_path': '/media/tudor1.mp4', 'metadata': {'año': '20XX', 'director': 'Un señor', 'capitulos': '12'}},
            {'id': 3, 'title': 'CHERNBOBYL', 'rating': 9, 'channel': 2, 'content_path': '/media/chernobyl1.mp4', 'metadata': {'año': '20XX', 'director': 'Otro señor', 'capitulos': '12'}},
            {'id': 4, 'title': 'SOÑANDO SOÑANDO TRIUNFÉ AMETRALLANDO', 'rating': 7, 'channel': 3, 'content_path': '/media/dream.mp4', 'metadata': {'Idiomas': '7', 'director': 'Un señor', 'capitulos': '12'}},
            {'id': 5, 'title': 'NAZI SCHOOL MUSICAL', 'rating': 6, 'channel': 3, 'content_path': '/media/school.mp4', 'metadata': {'subtitulos': 'Si', 'director': 'Un señor', 'capitulos': '12'}}]
        )

    def test_content_rating(self):
        #Testing if API can filter by rating. In this case, we use 7 as example
        response = self.client.get('/contents/7')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'id': 1, 'title': 'VIKINGS', 'rating': 8, 'channel': 2, 'content_path': '/media/vikings1.mp4', 'metadata': {'decripcion': 'los vikings', 'director': 'Un señor'}},
            {'id': 3, 'title': 'CHERNBOBYL', 'rating': 9, 'channel': 2, 'content_path': '/media/chernobyl1.mp4', 'metadata': {'año': '20XX', 'director': 'Otro señor', 'capitulos': '12'}},
            {'id': 4, 'title': 'SOÑANDO SOÑANDO TRIUNFÉ AMETRALLANDO', 'rating': 7, 'channel': 3, 'content_path': '/media/dream.mp4', 'metadata': {'Idiomas': '7', 'director': 'Un señor', 'capitulos': '12'}}]
        )