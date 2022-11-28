# Generated by Django 4.0.6 on 2022-11-28 12:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_location_address_location_isfree_location_plus_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.location')),
            ],
        ),
    ]