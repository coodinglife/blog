#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from ..models import Article, Category
from django import template

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.order_by('-create_time')[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('create_time', 'month', order="DESC")


@register.simple_tag
def get_categories():
    return Category.objects.all()




