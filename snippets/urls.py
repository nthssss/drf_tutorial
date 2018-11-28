# -*- coding: utf-8 -*-
__author__ = 'Niu Zhisheng'
__date__ = '2018/11/28 11:53'

from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
