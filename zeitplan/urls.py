from django.urls import path

from . import views

app_name = "zeitplan"
urlpatterns = [
    path("index/", views.index, name="index"),
    # path("overview/", views.OverviewView.as_view(), name="overview"),
    path("overview/", views.overview, name="overview"),
    path("new_day/", views.day_new, name="day_new"),
    path("add_new_day/", views.day_add_new, name="day_add_new"),
    path("<int:day_id>/", views.day_overview, name="day_overview"),
    path("<int:day_id>/delete/", views.day_delete, name="day_delete"),
    path("<int:day_id>/edit/", views.day_edit, name="day_edit"),
    path("<int:day_id>/votes/", views.day_editing, name="day_editing"),
    path("<int:day_id>/new_time_entry/", views.time_entry_add, name="time_entry_add"),
    path("<int:entry_id>/category_add/", views.category_add, name="category_add"),
    path("<int:entry_id>/add_time_frame/", views.add_time_frame, name="add_time_frame"),
]
