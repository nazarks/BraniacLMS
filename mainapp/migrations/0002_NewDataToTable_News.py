# Generated by Django 4.1.1 on 2022-09-26 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    def forwards_func(apps, schema_editor):
        # Get model
        News = apps.get_model("mainapp", "News")
        # Create model's objects
        News.objects.create(
            title="title 1",
            preambule="preambule 1",
            body="body 1",
        )
        News.objects.create(
            title="title 2",
            preambule="preambule 2",
            body="body 2",
        )
        News.objects.create(
            title="title 3",
            preambule="preambule 3",
            body="body 3",
        )
        News.objects.create(
            title="title 4",
            preambule="preambule 4",
            body="body 4",
        )
        News.objects.create(
            title="title 5",
            preambule="preambule 5",
            body="body 5",
        )
        News.objects.create(
            title="title 6",
            preambule="preambule 6",
            body="body 6",
        )

    def reverse_func(apps, schema_editor):
        # Get model
        News = apps.get_model("mainapp", "News")
        # Delete objects
        News.objects.all().delete()

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
