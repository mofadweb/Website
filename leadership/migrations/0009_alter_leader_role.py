# Generated by Django 3.2 on 2022-01-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadership', '0008_auto_20220126_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='role',
            field=models.CharField(max_length=255),
        ),
    ]
