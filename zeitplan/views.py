from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Day


def index(request):
    text = 'Hallo, das ist der aktuelle Prototyp der App "Zeitplan" ... in progress ... still'
    context = {"text": text}
    return render(request, "zeitplan/index.html", context)


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


def day_edit(request, day_id):
    context = get_time_entry_list(day_id)
    return render(request, "zeitplan/day_editing.html", context)


def day_votes(request, day_id):
    day = Day.objects.get(pk=day_id)
    try:
        if "entry_vote" in request.POST:
            print("VOTE")
            entries_votes = day.time_entry_set.get(pk=request.POST["entry_vote"])
        elif "entry_passed" in request.POST:
            print("PASSED")
            entries_passed = day.time_entry_set.get(pk=request.POST["entry_passed"])
    except (KeyError, Day.DoesNotExist):
        context = {"day": day, "error message": "Why?"}
        return render(request, "zeitplan/day_editing.html", context)
    else:
        if "entry_vote" in request.POST:
            entries_votes.votes += 1
            entries_votes.save()
        elif "entry_passed" in request.POST:
            if entries_passed.entry_passed is None:
                entries_passed.entry_passed = True
            else:
                entries_passed.entry_passed = None
            entries_passed.save()
        return HttpResponseRedirect(reverse("zeitplan:day_overview", args=(day.id,)))
