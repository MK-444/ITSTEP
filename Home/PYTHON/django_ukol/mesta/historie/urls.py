from django.urls import path
from . import views 


urlpatterns = [
    path("", views.index, name="index"),
    path("pocasi", views.pocasi, name="pocasi"),
    path("doprava", views.doprava, name="doprava"),
    path("<city>", views.zajmavost, name="mesto"),
    
]
