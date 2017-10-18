import django_tables2 as tables
from .models import Location


class LocationTable(tables.Table):

    class Meta:
        model = Location
        attrs = {
            ' class ': 'paleblue',
            ' order_by_field ': None,
            ' prefix ': None
        }


