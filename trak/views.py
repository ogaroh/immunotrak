# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def charts_view(request, *args, **kwargs):
    return render(request, "charts.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
