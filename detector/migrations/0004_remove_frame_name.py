# Generated by Django 4.2 on 2023-05-08 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0003_frame_prediction_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frame',
            name='name',
        ),
    ]
