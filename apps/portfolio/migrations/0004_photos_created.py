# Generated by Django 4.1.1 on 2022-09-13 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_photos_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
