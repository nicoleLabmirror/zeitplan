# Generated by Django 4.0.6 on 2022-08-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeitplan', '0003_remove_day_day_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='time_entry',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
