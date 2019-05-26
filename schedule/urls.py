from django.urls import path

from . import views
from .views import schedule_view

urlpatterns = [
    path('', schedule_view),
]
