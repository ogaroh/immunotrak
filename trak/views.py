# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from . import models as trak_models


class VaccineView(ListView):
    model = trak_models.Vaccine
    context_object_name =  'vaccine_list'
    template_name = 'home.html'


class LocationsView(ListView):
    model = trak_models.Location
    context_object_name =  'locations_list'
    template_name = 'locations.html'


class MedicalView(ListView):
    model = trak_models.Child
    context_object_name = 'children_list'
    template_name = 'medical.html'




# all charts view
def charts_view(request, *args, **kwargs):
    return render(request, "charts.html", {})

# online help view
def help_view(request, *args, **kwargs):
    return render(request, "help.html", {})

# contact us view
def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


# about immunotrak view
def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


# locations view
def locations_view(request, *args, **kwargs):
    return render(request, "locations.html", {})





# register view
def register_view(request):
    return render(request, "register.html", {})
