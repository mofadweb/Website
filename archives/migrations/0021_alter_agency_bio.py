# Generated by Django 3.2 on 2022-02-07 09:08

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0020_auto_20220127_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='bio',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
