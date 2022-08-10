from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Day, Time_entry


def index(request):
    text = 'Hallo, das ist der aktuelle Prototyp der App "Zeitplan ... in progress ... still"'
    context = {"text": text}
    return render(request, "zeitplan/index.html", context)

def overview(request):
    all_days_list = Day.objects.all().order_by("day_date")
    context = {"all_days_list": all_days_list}
    return render(request, "zeitplan/overview.html", context)

def day_overview(request, day_id):
    time_entry_list = Time_entry.objects.filter(
        day=day_id
    )
    context = {
        "time_entry_list": time_entry_list,
        "day_id": day_id
    }
    return render(request, "zeitplan/day_overview.html", context)

def day_edit(request, day_id):
    time_entry_list = Time_entry.objects.filter(
        day=day_id
    )
    day = Day.objects.get(pk=day_id)
    context = {
        "time_entry_list": time_entry_list,
        "day_id": day_id,
        "day_name": day.day_name,
    }
    return render(request, "zeitplan/day_editing.html", context)

def day_votes(request, day_id):
    day = Day.objects.get(pk=day_id)
    try:
        entries = day.time_entry_set.get(pk=request.POST["entry"])
    except (KeyError, Day.DoesNotExist):
        context = {
            "day_id": day_id,
            "error message": "Why?"
        }
        return render(request, "zeitplan/day_editing.html", context)
    else:
        entries.votes += 1
        entries.save()
        return HttpResponseRedirect(
            reverse(
                "zeitplan:day_overview",
                args=(day_id,)
            )
        )
