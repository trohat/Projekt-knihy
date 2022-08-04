from django.urls import path

from . import views

urlpatterns = [
    path("", views.pridat_knihu, name="pridat"),
    path("dekuji", views.dekuji, name="dekuji")   
]
