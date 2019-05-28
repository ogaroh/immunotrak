# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# home view
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


# all charts view
def charts_view(request, *args, **kwargs):
    return render(request, "charts.html", {})


# contact us view
def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


# about immunotrak view
def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


# locations view
def locations_view(request, *args, **kwargs):
    return render(request, "locations.html", {})


# medical view
def medical_view(request, *args, **kwargs):
    return render(request, "medical.html", {})



# register view
def register_view (request):
    return render(request, "register.html", {})


