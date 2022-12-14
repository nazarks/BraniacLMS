# Generated by Django 4.1.1 on 2022-09-30 19:23

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="customuser",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("username"),
                name="username_case_insensitive",
            ),
        ),
    ]
