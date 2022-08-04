from django.db import models
from own_modules import german_translation_for_day_name


class Day(models.Model):
    day_date = models.DateField(null=True, default=None)

    @property
    def day_name(self):
        day_name_english = self.day_date.strftime("%A")
        day_name_german = german_translation_for_day_name[day_name_english]
        return day_name_german

    def __str__(self):
        return f"Datum: {self.day_date}"


class Time_entry(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    entry_text = models.CharField(max_length=100)
    entry_passed = models.BooleanField(null=True, default=None)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Tätigkeit: {self.entry_text}"
