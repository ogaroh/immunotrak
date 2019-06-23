# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import LocationForm

def get_location(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LocationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LocationForm()

    return render(request, 'location_posted.html', {'form': form})


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


