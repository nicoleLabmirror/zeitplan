from django.shortcuts import render
from django.http import HttpResponse
from .models import Day


def index(request):
    return HttpResponse('Hallo, das ist der aktuelle Prototyp der App "Zeitplan".')

def overview(request):
    all_days_list = Day.objects.all().order_by("day_date")
    context = {"all_days_list": all_days_list}
    return render(request, "zeitplan/overview.html", context)

def day_overview(request, day_id):
    model = Day
    d = Day.objects.get(pk=day_id)
    response = f"Tag: {d.day_name}. Datum: {d.day_date}."
    return HttpResponse(response)

def day_time_entries(request, day_id):
    model = Day
    time_entry_list = list(
        Day.objects.get(pk=day_id).time_entry_set.all().values_list("entry_text")
    )
    response = f"Das sind Tätigkeiten: {time_entry_list}"
    return HttpResponse(response)
