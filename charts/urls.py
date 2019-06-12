from django.urls import path
from django.conf.urls import url

from . import views
from .views import get_data, ChartsView, ChartData

urlpatterns = [
    path('chart/', ChartsView.as_view()),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
]
