#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('article/<int:article_pk>', views.article_comment, name='article_comment')
]
