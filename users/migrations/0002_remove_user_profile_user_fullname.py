# Generated by Django 4.1.2 on 2022-10-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="profile",),
        migrations.AddField(
            model_name="user",
            name="fullname",
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
