# Generated by Django 4.1.1 on 2022-09-14 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_photos_options_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='portfolio.photos'),
        ),
    ]
