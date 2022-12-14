# Generated by Django 4.0.6 on 2022-11-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(default='Nie określony', max_length=100),
        ),
        migrations.AddField(
            model_name='location',
            name='isFree',
            field=models.CharField(choices=[('free', 'Free'), ('paid', 'Paid'), ('unknown', 'Unknown')], default='Unknown', max_length=7),
        ),
        migrations.AddField(
            model_name='location',
            name='plus_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
