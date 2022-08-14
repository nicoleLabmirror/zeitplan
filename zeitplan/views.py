from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Day


def index(request):
    return render(request, "zeitplan/index.html")


class OverviewView(generic.ListView):
    template_name = "zeitplan/overview.html"
    context_object_name = "all_days_list"

    def get_queryset(self):
        all_days_list = Day.objects.all().order_by("day_date")
        return all_days_list


def get_time_entry_list(day_id):
    day = Day.objects.get(pk=day_id)
    time_entry_list = day.time_entry_set.all()
    context = {
        "day": day,
        "time_entry_list": time_entry_list,
    }
    return context


# TODO DetailView?
def day_overview(request, day_id):
    context = get_time_entry_list(day_id)
    return render(request, "zeitplan/day_overview.html", context)


# Editing entry
def day_edit(request, day_id):
    context = get_time_entry_list(day_id)
    return render(request, "zeitplan/day_editing.html", context)


def day_votes(request, day_id):
    day = Day.objects.get(pk=day_id)
    # TODO using 'if "entry ..." twice doesn't seem like a proper solution
    try:
        if "entry_vote" in request.POST:
            entries = day.time_entry_set.get(pk=request.POST["entry_vote"])
        elif "entry_passed" in request.POST:
            entries = day.time_entry_set.get(pk=request.POST["entry_passed"])
    except (KeyError, Day.DoesNotExist):
        context = {"day": day, "error message": "Why?"}
        return render(request, "zeitplan/day_editing.html", context)
    else:
        if "entry_vote" in request.POST:
            entries.votes += 1
            entries.save()
        elif "entry_passed" in request.POST:
            if entries.entry_passed is None:
                entries.entry_passed = True
            else:
                entries.entry_passed = None
            entries.save()
        return HttpResponseRedirect(reverse("zeitplan:day_edit", args=(day.id,)))


# Add new day
def day_new(request):
    return render(request, "zeitplan/day_new.html")


def day_add_new(request):
    new_day = Day(day_date=request.POST["new_day"])
    new_day.save()

    return HttpResponseRedirect(reverse("zeitplan:overview"))


# Delete day
def day_delete(request, day_id):
    day_deleting = Day.objects.get(pk=day_id)
    day_deleting.delete()

    return HttpResponseRedirect(reverse("zeitplan:overview"))


# Add new time entry
def time_entry_add(request, int_day_id):
    print(int_day_id, request.POST["entry_add"])
    day = Day.objects.get(pk=int_day_id)
    new_entry = day.time_entry_set.create(entry_text=request.POST["entry_add"])
    new_entry.save()
    return HttpResponseRedirect(reverse("zeitplan:day_edit", args=(day.id,)))
