# Generated by Django 3.2 on 2022-01-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('Blog', 'Blog'), ('Press release', 'Press release')], default='Blog', max_length=25),
        ),
    ]