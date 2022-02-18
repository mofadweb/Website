# Generated by Django 3.2 on 2021-04-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0014_alter_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('image', models.FileField(null=True, upload_to='patron_images')),
                ('location', models.CharField(max_length=70)),
            ],
        ),
    ]