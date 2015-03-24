# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from charts import views

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=views.ChartListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<title>[^/]+)/$',
        view=views.ChartDetailView.as_view(),
        name='detail'
    ),
)
