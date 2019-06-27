from django.urls import path
from . import views

from .views import get_data, ChartsView, EverythingChartData, LocationChartData, ChildrenView, ParentView, VaccineView, LocationView
urlpatterns = [
    path('', ChartsView.as_view(), name="charts"),
    path('tables/children/', ChildrenView.as_view()),
    path('tables/vaccines/', VaccineView.as_view()),
    path('tables/parents/', ParentView.as_view()),
    path('tables/locations/', LocationView.as_view()),

    path('api/data/', get_data, name="api-data"),  # endpoint 1
    path('api/chart/data/', EverythingChartData.as_view()),  # endpoint 2
    path('api/location-chart/data/', LocationChartData.as_view()),  # endpoint 2
]
