# Generated by Django 4.0.6 on 2022-08-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeitplan', '0004_time_entry_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=100)),
            ],
        ),
    ]
