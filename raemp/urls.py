from django.conf.urls import url
from django.contrib import admin
from raemp.views import LocationCreateView,LocationDeleteView,LocationUpdateView,LocationListView,LocationTableView

app_name = 'raemp'

urlpatterns = [
    #住所関連URL
    url(r'^location/list$', LocationListView.as_view()),
    url(r'^location/table$', LocationTableView.as_view()),
    url(r'^location/create$', LocationCreateView.as_view()),
    url(r'^location/(?P<pk>\d+)/update$', LocationUpdateView.as_view()),
    url(r'^location/(?P<pk>\d+)/delete$', LocationDeleteView.as_view()),
]

