from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import View

from trak import models as trak_models


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "data": [12, 19, 3, 5, 2, 3, 10],
        }

        return Response(data)



class ChartsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html')
