from django_tables2 import SingleTableView

from raemp.tables import *
from .forms import *
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Location


# 住所関連Viewクラス

class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = "raemp/location_form.html"

    def get_success_url(self):

        # 成功時にリダイレクトするURL
        return "/raemp/location/table"

class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = "raemp/location_form.html"
    success_url = "/raemp/location/table"  # 成功時にリダイレクトするURL


class LocationDeleteView(DeleteView):
    model = Location
    success_url = "/raemp/location/table"  # 成功時にリダイレクトするURL


class LocationTableView(SingleTableView):
    model = Location
    table_class = LocationTable

    def get_template_names(self):
        return "raemp/location_table.html"

# 店舗関連Viewクラス

class ShopTableView(SingleTableView):
    model = Shop
    table_class = ShopTable

    def get_template_names(self):
        return "raemp/shop_table.html"

class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm
    template_name = "raemp/shop_form.html"
    success_url = "/raemp/shop/table"  # 成功時にリダイレクトするURL


class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = "raemp/shop_form.html"
    success_url = "/raemp/shop/table"  # 成功時にリダイレクトするURL


class ShopDeleteView(DeleteView):
    model = Shop
    success_url = "/raemp/shop/table"  # 成功時にリダイレクトするURL