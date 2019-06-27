from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View, ListView

# models
from trak import models as trak_models
from schedule import models as schedule_models


Vaccines = trak_models.Vaccine
Parents = trak_models.Parent
Children = trak_models.Kid
Counties = trak_models.Location

Schedules = schedule_models.Schedule


class ChildrenView(ListView):
    model = trak_models.Kid
    context_object_name = 'children_list'
    template_name = 'tables.html'



class ParentView(ListView):
    model = trak_models.Parent
    context_object_name = 'parent_list'
    template_name = 'parent_list.html'


class LocationView(ListView):
    model = trak_models.Location
    context_object_name = 'parent_list'
    template_name = 'location_list.html'


class VaccineView(ListView):
    model = trak_models.Vaccine
    context_object_name = 'parent_list'
    template_name = 'vaccine_list.html'



# queryset counts
vaccines_qs_count = Vaccines.objects.all().count()
parents_qs_count = Parents.objects.all().count()
children_qs_count =  Children.objects.all().count()
locations_qs_count  = Counties.objects.all().count()
schedules_qs_count = Schedules.objects.all().count()

# get a list of all locations and vaccines
locations = serializers.serialize("json", Counties.objects.all())

class ChartsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html')


def get_data(request, *args, **kwargs):
    data = {
        "vaccines": 7,
        "kids": 15,
    }
    return JsonResponse(data)


class EverythingChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        labels = ['Vaccines', 'Children', 'Parents', 'Appointments', 'Locations']
        default_items = [vaccines_qs_count, children_qs_count, parents_qs_count,schedules_qs_count, locations_qs_count]
       
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


class LocationChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        location_items = [locations]

        location_data = {
            "labels": location_items,
            "default": location_items,
        }
        return Response(location_data)

