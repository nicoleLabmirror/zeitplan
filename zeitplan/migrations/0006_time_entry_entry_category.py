# Generated by Django 4.0.6 on 2022-08-06 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zeitplan', '0005_entry_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='time_entry',
            name='entry_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zeitplan.entry_category'),
        ),
    ]
