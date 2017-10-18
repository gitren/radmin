from django_tables2 import RequestConfig, SingleTableView

from raemp.tables import LocationTable
from .forms import *
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, TemplateView
from .models import Location


# 住所関連Viewクラス

class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = "raemp/location_form.html"
    success_url = "/raemp/location/list"  # 成功時にリダイレクトするURL


class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = "raemp/location_form.html"
    success_url = "/raemp/location/list"  # 成功時にリダイレクトするURL


class LocationDeleteView(DeleteView):
    model = Location
    success_url = "/raemp/location/list"  # 成功時にリダイレクトするURL


class LocationListView(ListView):
    model = Location

    def get_template_names(self):
        return "raemp/location_table.html"

    def get_queryset(self):
        return Location.objects.all()


class LocationTableView(SingleTableView):
    model = Location
    table_class = LocationTable

    # def get_queryset(self):
    #    return Location.objects.all()

    def get_template_names(self):
        return "raemp/location_table.html"

        # def get_table(self, **kwargs):
        #     return LocationTable

        # def get_table_data(self):
        #    return Location.objects.all()

        # def get_table_kwargs(self):
        #    return {
        #        'class': 'paleblue'
        #    }
