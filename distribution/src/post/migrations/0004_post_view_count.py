# Generated by Django 4.1.6 on 2023-02-13 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0003_author_profile_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="post", name="view_count", field=models.IntegerField(default=0),
        ),
    ]
