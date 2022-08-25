from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('temp', views.temp_view),
    path('temp_new', views.temp_view_advance,name="new")
]