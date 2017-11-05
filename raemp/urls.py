from django.conf.urls import url
from raemp.views import *

app_name = 'raemp'

urlpatterns = [
    # 住所関連URL
    url(r'^location/table$', LocationTableView.as_view()),
    url(r'^location/create$', LocationCreateView.as_view()),
    url(r'^location/update/(?P<pk>\d+)/$', LocationUpdateView.as_view(), name='location_update'),
    url(r'^location/delete/(?P<pk>\d+)/$', LocationDeleteView.as_view(), name='location_delete'),
    # 店舗関連URL
    url(r'^shop/table$', ShopTableView.as_view()),
    url(r'^shop/create$', ShopCreateView.as_view()),
    url(r'^shop/update/(?P<pk>\d+)/$', ShopUpdateView.as_view(), name='shop_update'),
    url(r'^shop/delete/(?P<pk>\d+)/$', ShopDeleteView.as_view(), name='shop_delete'),
    # 店舗関連URL
    url(r'^person/table$', PersonTableView.as_view()),
    url(r'^person/create$', PersonCreateView.as_view()),
    url(r'^person/update/(?P<pk>\d+)/$', PersonUpdateView.as_view(), name='person_update'),
    url(r'^person/delete/(?P<pk>\d+)/$', PersonDeleteView.as_view(), name='person_delete'),
    # 画像関連URL
    url(r'^image/table$', ImageTableView.as_view()),
    url(r'^image/create$', ImageCreateView.as_view()),
    url(r'^image/update/(?P<pk>\d+)/$', ImageUpdateView.as_view(), name='image_update'),
    url(r'^image/delete/(?P<pk>\d+)/$', ImageDeleteView.as_view(), name='image_delete'),
]