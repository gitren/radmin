import django_tables2 as tables
from django_tables2.utils import A
from .models import Location, Shop



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





