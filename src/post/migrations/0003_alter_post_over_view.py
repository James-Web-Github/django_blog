# Generated by Django 4.2 on 2023-04-17 15:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='over_view',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300),
        ),
    ]