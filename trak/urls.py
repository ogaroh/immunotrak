from django.urls import path

from . import views as trak_view
from .views import contact_view, about_view, locations_view, MedicalView, register_view, VaccineView

urlpatterns = [
    path('', trak_view.VaccineView.as_view(), name='home'),
    path('home/',trak_view.VaccineView.as_view()),
    # path('charts/', charts_view),
    path('contact/', contact_view),
    path('about/', about_view),
    path('locations/', locations_view),
    path('medical/', trak_view.MedicalView.as_view()),
    path('medical/register/', register_view),
    path('help/', trak_view.help_view),
]
