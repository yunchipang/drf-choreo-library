# Generated by Django 4.1.7 on 2023-02-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("choreos", "0002_alter_choreography_style"),
    ]

    operations = [
        migrations.AlterField(
            model_name="choreography",
            name="video_url",
            field=models.URLField(blank=True, default="", max_length=100),
        ),
    ]
