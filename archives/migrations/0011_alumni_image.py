# Generated by Django 3.2 on 2021-04-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0010_auto_20210420_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='image',
            field=models.FileField(null=True, upload_to='alumni_images'),
        ),
    ]
