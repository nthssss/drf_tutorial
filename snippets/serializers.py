# -*- coding: utf-8 -*-
__author__ = 'Niu Zhisheng'
__date__ = '2018/11/28 11:18'
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
