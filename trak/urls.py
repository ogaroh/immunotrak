from django.urls import path

from . import views
from .views import home_view, charts_view, contact_view, about_view, schedule_view, locations_view, register_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view),
    path('charts/', charts_view),
    path('contact/', contact_view),
    path('about/', about_view),
    path('schedule/', schedule_view),
    path('locations/', locations_view),
    path('register/', register_view),
]
