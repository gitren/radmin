from .forms import *
from django.views.generic import CreateView,DeleteView,ListView,UpdateView

#住所関連Viewクラス

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
