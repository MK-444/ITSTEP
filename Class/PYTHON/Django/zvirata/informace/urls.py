from unicodedata import name
from django.urls import path 
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("slon", views.slon),
    path("zirafa", views.zirafa),
    path("informace/<str:zvire>", views.informace, name="popis_zvirate")
]
# path converter

# tohle je ROUTER (cesky smerovac)