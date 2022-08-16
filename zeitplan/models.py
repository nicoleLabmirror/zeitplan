from django.db import models

from .own_modules import get_german_day_name


class Day(models.Model):
    day_date = models.DateField(null=True, default=None)

    @property
    def day_name(self):
        day_name_english = self.day_date.strftime("%A")
        day_name_german = get_german_day_name(day_name_english)
        return day_name_german

    @property
    def different_day_date(self):
        diff_day_date = self.day_date.strftime("%d" "." "%m" "." "%Y")
        return diff_day_date

    def __str__(self):
        return f"Datum: {self.day_date}"


class Entry_category(models.Model):
    category_text = models.CharField(max_length=100)

    def __str__(self):
        return f"Kategorie: {self.category_text}"


class Time_entry(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    entry_category = models.ForeignKey(
        Entry_category, models.SET_NULL, blank=True, null=True
    )
    entry_text = models.CharField(max_length=100)
    entry_passed = models.BooleanField(null=True, default=None)
    votes = models.IntegerField(default=0)
    start_of_entry = models.DateTimeField(null=True, default=None)
    end_of_entry = models.DateTimeField(null=True, default=None)

    @property
    def entry_status(self):
        if self.entry_passed is None:
            entry_status = "Nicht erledigt"
        else:
            entry_status = "Erledigt"
        return entry_status

    @property
    def proper_time_format(self):
        if self.start_of_entry and self.end_of_entry is not None:
            start = self.start_of_entry.strftime("%H" ":" "%M")
            end = self.end_of_entry.strftime("%H" ":" "%M")
            return start, end

    def __str__(self):
        return f"Tätigkeit: {self.entry_text}"
