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
    # 個人関連URL
    url(r'^person/table$', PersonTableView.as_view()),
    url(r'^person/create$', PersonCreateView.as_view()),
    url(r'^person/update/(?P<pk>\d+)/$', PersonUpdateView.as_view(), name='person_update'),
    url(r'^person/delete/(?P<pk>\d+)/$', PersonDeleteView.as_view(), name='person_delete'),
    # 画像関連URL
    url(r'^image/table$', ImageTableView.as_view()),
    url(r'^image/create$', ImageCreateView.as_view()),
    url(r'^image/update/(?P<pk>\d+)/$', ImageUpdateView.as_view(), name='image_update'),
    url(r'^image/delete/(?P<pk>\d+)/$', ImageDeleteView.as_view(), name='image_delete'),
    # 月間カレンダー関連URL
    url(r'^monthlycalendar$', MonthlyCalendarView.as_view(), name='monthlycalendar'),
    url(r'^monthlycalendar(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', MonthlyCalendarView.as_view(), name='monthlycalendar'),
    # 週間カレンダー関連URL
    url(r'^weeklycalendar$', WeeklyCalendarView.as_view(), name='weeklycalendar'),
    url(r'^weeklycalendar(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<week>[0-9]+)/$',
        WeeklyCalendarView.as_view(),
        name='weeklycalendar'
    ),
    # シフト関連URL
    url(
        (
            r'^shift_create/'
            r'(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$'
        ),
        ShiftCreateView.as_view(),
        name='shift_create'),
    url(
        (
            r'^shift_list/'
            r'(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$'
        ),
        ShiftListView.as_view(),
        name='shift_list'),
    # 派遣要員関連URL
    url(r'^tempstaff/table$', TempStaffTableView.as_view()),
    url(r'^tempstaff/create$', TempStaffCreateView.as_view()),
    url(r'^tempstaff/update/(?P<pk>\d+)/$', TempStaffUpdateView.as_view(), name='tempstaff_update'),
    url(r'^tempstaff/delete/(?P<pk>\d+)/$', TempStaffDeleteView.as_view(), name='tempstaff_delete'),
]
