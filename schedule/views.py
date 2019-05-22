# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


# schedules view
def schedule_view(request, *args, **kwargs):
    return render(request, "schedule.html", {})
