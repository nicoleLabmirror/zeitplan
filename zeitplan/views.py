from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# from django.views import generic

from .models import Day, EntryCategory, TimeEntry


def index(request):
    return render(request, "zeitplan/index.html")


def get_time_entry_list(day_id):
    day = Day.objects.get(pk=day_id)
    time_entry_list = day.timeentry_set.all().order_by("start_of_entry")
    context = {
        "day": day,
        "time_entry_list": time_entry_list,
    }
    return context


# class OverviewView(generic.ListView):
#     template_name = "zeitplan/overview.html"
#     context_object_name = "all_days_list"
#
#     def get_queryset(self):
#         all_days_list = Day.objects.all().order_by("day_date")
#        return all_days_list


@login_required
def overview(request):
    all_days = Day.objects.all().order_by("day_date")
    context = {"all_days_list": all_days}
    return render(request, "zeitplan/overview.html", context)


@login_required
def day_overview(request, day_id):
    print(request)
    context = get_time_entry_list(day_id)
    return render(request, "zeitplan/day_overview.html", context)


@login_required
def day_edit(request, day_id):
    context = get_time_entry_list(day_id)
    return render(request, "zeitplan/day_editing.html", context)


@login_required
def day_editing(request, day_id):
    try:
        if "entry_vote" in request.POST:
            entries = Day.objects.get(pk=day_id).timeentry_set.get(
                pk=request.POST["entry_vote"]
            )
        elif "entry_passed" in request.POST:
            entries = Day.objects.get(pk=day_id).timeentry_set.get(
                pk=request.POST["entry_passed"]
            )
        elif "entry_delete" in request.POST:
            entries = Day.objects.get(pk=day_id).timeentry_set.get(
                pk=request.POST["entry_delete"]
            )
    except (KeyError, Day.DoesNotExist):
        context = {"day": Day.objects.get(pk=day_id), "error message": "Why?"}
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
        elif "entry_delete" in request.POST:
            entries.delete()
        return HttpResponseRedirect(
            reverse("zeitplan:day_edit", args=(Day.objects.get(pk=day_id).id,))
        )


@login_required
def category_add(request, entry_id):
    entry = TimeEntry.objects.get(pk=entry_id)
    new_category = EntryCategory(category_text=request.POST["category_add"])
    new_category.save()
    entry.entry_category = new_category
    entry.save()
    return HttpResponseRedirect(reverse("zeitplan:day_edit", args=(entry.day.id,)))


@login_required
def add_time_frame(request, entry_id):
    entry = TimeEntry.objects.get(pk=entry_id)
    entry.start_of_entry = "%sT%s" % (
        entry.day.day_date,
        request.POST["add_time_frame_start"],
    )
    entry.end_of_entry = "%sT%s" % (
        entry.day.day_date,
        request.POST["add_time_frame_end"],
    )
    entry.save()
    return HttpResponseRedirect(reverse("zeitplan:day_edit", args=(entry.day.id,)))


@login_required
def day_new(request):
    return render(request, "zeitplan/day_new.html")


@login_required
def day_add_new(request):
    new_day = Day(day_date=request.POST["new_day"])
    new_day.save()
    return HttpResponseRedirect(reverse("zeitplan:overview"))


@login_required
def day_delete(request, day_id):
    day_deleting = Day.objects.get(pk=day_id)
    day_deleting.delete()
    return HttpResponseRedirect(reverse("zeitplan:overview"))


@login_required
def time_entry_add(request, day_id):
    new_entry = Day.objects.get(pk=day_id).timeentry_set.create(
        entry_text=request.POST["entry_add"]
    )
    new_entry.save()
    return HttpResponseRedirect(reverse("zeitplan:day_edit", args=(new_entry.day.id,)))
