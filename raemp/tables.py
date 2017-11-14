import django_tables2 as tables
from django_tables2.utils import A
from .models import *


class LocationTable(tables.Table):
    u_check = tables.LinkColumn(
        'raemp:location_update', args=[A('pk')], text='変更', current_app='raemp', verbose_name='変更')
    d_check = tables.LinkColumn(
        'raemp:location_delete', args=[A('pk')], text='削除', current_app='raemp', verbose_name='削除')

    class Meta:
        model = Location
        attrs = {
            ' class ': 'paleblue',
            ' order_by_field ': None,
            ' prefix ': None
        }


class ShopTable(tables.Table):
    u_check = tables.LinkColumn(
        'raemp:shop_update', args=[A('pk')], text='変更', current_app='raemp', verbose_name='変更')
    d_check = tables.LinkColumn(
        'raemp:shop_delete', args=[A('pk')], text='削除', current_app='raemp', verbose_name='削除')

    class Meta:
        model = Shop
        attrs = {
            ' class ': 'paleblue',
            ' order_by_field ': None,
            ' prefix ': None
        }


class PersonTable(tables.Table):
    u_check = tables.LinkColumn(
        'raemp:person_update', args=[A('pk')], text='変更', current_app='raemp', verbose_name='変更')
    d_check = tables.LinkColumn(
        'raemp:person_delete', args=[A('pk')], text='削除', current_app='raemp', verbose_name='削除')

    class Meta:
        model = Person
        attrs = {
            ' class ': 'paleblue',
            ' order_by_field ': None,
            ' prefix ': None
        }


class ImageTable(tables.Table):
    # imagelink = tables.TemplateColumn(
    #     '<a href="/media/{{record.image_file}}"><img src="{{record.small.url}}" /></a>', verbose_name='画像')
    imagelink = tables.TemplateColumn(
        """<a href="javascript:void(0); \
        window.open('/media/{{record.image_file}}','subwin','width=500,height=500');"> \
        <img src="{{record.small.url}}" /></a>""",
        verbose_name='画像')

    u_check = tables.LinkColumn(
        'raemp:image_update', args=[A('pk')], text='変更', current_app='raemp', verbose_name='変更')
    d_check = tables.LinkColumn(
        'raemp:image_delete', args=[A('pk')], text='削除', current_app='raemp', verbose_name='削除')

    class Meta:
        model = Image
        attrs = {
            ' class ': 'paleblue',
            ' order_by_field ': None,
            ' prefix ': None
        }


class TempStaffTable(tables.Table):
    u_check = tables.LinkColumn(
        'raemp:tempstaff_update', args=[A('pk')], text='変更', current_app='raemp', verbose_name='変更')
    d_check = tables.LinkColumn(
        'raemp:tempstaff_delete', args=[A('pk')], text='削除', current_app='raemp', verbose_name='削除')

    class Meta:
        model = TempStaff
        attrs = {
            ' class ': 'paleblue',
            ' order_by_field ': None,
            ' prefix ': None
        }
