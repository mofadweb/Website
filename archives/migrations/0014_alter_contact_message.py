# Generated by Django 3.2 on 2021-04-23 14:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0013_patron_occupational_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]