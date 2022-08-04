from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("overview/", views.overview, name="overview"),
    path("<int:day_id>/", views.day_overview, name="day_overview"),
]
