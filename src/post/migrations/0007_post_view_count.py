# Generated by Django 4.2 on 2023-04-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
