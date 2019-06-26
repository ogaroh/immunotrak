from django.urls import path

from .views import ChartData, ChartsView

urlpatterns = [
    path('', ChartsView.as_view(), name="charts"),
    path('api/chart/data/', ChartData.as_view()),  # new
]
