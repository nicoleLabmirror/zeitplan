from django.urls import path

from . import views

app_name = "zeitplan"
urlpatterns = [
    path("", views.index, name="index"),
    path("overview/", views.OverviewView.as_view(), name="overview"),
    path("<int:day_id>/", views.day_overview, name="day_overview"),
    path("<int:day_id>/edit/", views.day_edit, name="day_edit"),
    path("<int:day_id>/votes/", views.day_votes, name="day_votes"),
]
