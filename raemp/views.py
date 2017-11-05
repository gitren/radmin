from django_tables2 import SingleTableView

from raemp.tables import *
from .forms import *
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import *


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


# 個人関連Viewクラス

class PersonTableView(SingleTableView):
    model = Person
    table_class = PersonTable

    def get_template_names(self):
        return "raemp/person_table.html"


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "raemp/person_form.html"
    success_url = "/raemp/person/table"  # 成功時にリダイレクトするURL


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "raemp/person_form.html"
    success_url = "/raemp/person/table"  # 成功時にリダイレクトするURL


class PersonDeleteView(DeleteView):
    model = Person
    success_url = "/raemp/person/table"  # 成功時にリダイレクトするURL


# 画像関連Viewクラス

class ImageTableView(SingleTableView):
    model = Image
    table_class = ImageTable

    def get_template_names(self):
        return "raemp/image_table.html"

class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm
    template_name = "raemp/image_form.html"
    success_url = "/raemp/image/table"  # 成功時にリダイレクトするURL

class ImageUpdateView(UpdateView):
    model = Image
    form_class = ImageForm
    template_name = "raemp/image_form.html"
    success_url = "/raemp/image/table"  # 成功時にリダイレクトするURL


class ImageDeleteView(DeleteView):
    model = Image
    success_url = "/raemp/image/table"  # 成功時にリダイレクトするURL