# Generated by Django 5.0.6 on 2024-06-11 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogpost",
            old_name="view_count",
            new_name="views",
        ),
    ]
