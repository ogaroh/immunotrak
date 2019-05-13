from django.urls import path

from . import views
from .views import home_view, login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view),
    path('login/', login_view),
]
