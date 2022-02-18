# Generated by Django 3.2 on 2022-01-27 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0019_auto_20220124_0352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agencyleader',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='agencyleader',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]