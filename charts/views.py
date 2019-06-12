from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


User = get_user_model()
# charts view


class ChartsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html', {})


def get_data(request, *args, **kwargs):
    data = {
        "vaccines": 7,
        "children": 100,
    }
    return JsonResponse(data)


# rest framework
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "vaccines": 7,
            "children": 100,
            "users": User.objects.all().count(),
        }
        return Response(data)
