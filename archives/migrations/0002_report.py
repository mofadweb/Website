# Generated by Django 3.2 on 2021-04-19 20:02

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Budget', 'Budget Statement'), ('NEC & G.A', 'NEC & G.A Meeting'), ('Financial', 'Financial Statement')], default='Budget', max_length=25)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
