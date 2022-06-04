#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Filename: d:\pgala\Pedro\proyectos\immfly\immfly_api\views.py
# Path: d:\pgala\Pedro\proyectos\immfly\immfly_api
# Created Date: Friday, June 3rd 2022, 6:02:52 pm
# Author: Pedro Gal�n P�rez
# 
# Copyright (c) 2022 Immfly.
###

from importlib.resources import contents
from django.http import JsonResponse
from .models import Content, Channel
from .serializers import ContentSerializer, ChannelSerializer

def content_list(request):
    #This gets all the Contents
    #Serializes them
    #Return json

    contents = Content.objects.all()
    serializer = ContentSerializer(contents, many=True)
    return JsonResponse(serializer.data, safe=False)


def channel_list(request):
    #This gets all the Channels
    #Serializes them
    #Return json

    channels = Channel.objects.all()
    serializer = ChannelSerializer(channels, many=True)
    return JsonResponse(serializer.data, safe=False)

def channel_subchannels(request, name):
    #This gets all the subChannels and the channel given a channel name
    #Serializes them
    #Return json

    channel = Channel.objects.filter(name__icontains=name)
    if channel:
        childrens = channel[0].get_all_children()
        serializer = ChannelSerializer(childrens, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({})

def content_by_rating(request, rating):
    #This gets all the contents which rating is greater than the argument
    #Serializes them
    #Return json

    contents = Content.objects.filter(rating__gte=rating)
    serializer = ContentSerializer(contents, many=True)
    return JsonResponse(serializer.data, safe=False)

def content_by_channel(request, name):
    #This gets all the contents given a channel name
    #Serializes them
    #Return json

    channel = Channel.objects.filter(name__icontains=name)
    if channel:
        contents = Content.objects.filter(channel=channel[0])
        serializer = ContentSerializer(contents, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({})
