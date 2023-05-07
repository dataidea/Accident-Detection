# Generated by Django 4.2 on 2023-05-07 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='date_time',
        ),
        migrations.AddField(
            model_name='prediction',
            name='date',
            field=models.CharField(default='not_set', max_length=255),
        ),
        migrations.AddField(
            model_name='prediction',
            name='time',
            field=models.CharField(default='not_set', max_length=255),
        ),
    ]
