from django.conf.urls import url
from django.contrib import admin
from raemp.views import *

app_name = 'raemp'

urlpatterns = [
    #住所関連URL
    # url(r'^location/list$', LocationListView.as_view()),
    url(r'^location/table$', LocationTableView.as_view()),
    url(r'^location/create$', LocationCreateView.as_view()),
    url(r'^location/update/(?P<pk>\d+)/$', LocationUpdateView.as_view(), name='location_update'),
    url(r'^location/delete/(?P<pk>\d+)/$', LocationDeleteView.as_view(), name='location_delete'),
    #店舗関連URL
    # url(r'^location/list$', LocationListView.as_view()),
    url(r'^shop/table$', ShopTableView.as_view()),
    url(r'^shop/create$', ShopCreateView.as_view()),
    url(r'^shop/update/(?P<pk>\d+)/$', ShopUpdateView.as_view(), name='shop_update'),
    url(r'^shop/delete/(?P<pk>\d+)/$', ShopDeleteView.as_view(), name='shop_delete'),
]

