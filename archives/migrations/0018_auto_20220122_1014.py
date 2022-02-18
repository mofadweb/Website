# Generated by Django 3.2 on 2022-01-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0017_alter_report_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AgencyLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(null=True, upload_to='agencyLeader_images')),
                ('position', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='agency',
            name='image',
            field=models.FileField(null=True, upload_to='agency_images'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='report',
            name='by',
            field=models.CharField(default='', max_length=80),
        ),
    ]