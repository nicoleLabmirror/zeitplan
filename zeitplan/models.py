from django.db import models


class Day(models.Model):
    day_date = models.DateField(null=True, default=None)

    @property
    def day_name(self):
        return self.day_date.strftime("%A")

    def __str__(self):
        return f"Datum: {self.day_date}"


class Time_entry(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    entry_text = models.CharField(max_length=100)
    entry_passed = models.BooleanField(null=True, default=None)

    def __str__(self):
        return f"Tätigkeit: {self.entry_text}"
