# Generated by Django 4.1.1 on 2022-09-13 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_photos_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
