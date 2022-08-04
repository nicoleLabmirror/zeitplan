from django.shortcuts import render
from django.http import HttpResponse
from .models import Day


def index(request):
    text = 'Hallo, das ist der aktuelle Prototyp der App "Zeitplan ... in progress ... still"'
    context = {"text": text}
    return render(request, "zeitplan/index.html", context)

def overview(request):
    all_days_list = Day.objects.all().order_by("day_date")
    context = {"all_days_list": all_days_list}
    return render(request, "zeitplan/overview.html", context)

def day_overview(request, day_id):
    model = Day
    time_entry_list = Day.objects.get(pk=day_id).time_entry_set.all()
    context = {"time_entry_list": time_entry_list}
    return render(request, "zeitplan/day_overview.html", context)
