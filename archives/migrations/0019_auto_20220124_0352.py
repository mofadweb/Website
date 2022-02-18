# Generated by Django 3.2 on 2022-01-24 03:52

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0018_auto_20220122_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('image', models.FileField(null=True, upload_to='project_images')),
                ('details', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('slug', models.SlugField(default='Will-be-added-when-saved')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='agency',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='slug',
            field=models.SlugField(default='Will-be-added-when-saved'),
        ),
        migrations.AddField(
            model_name='agencydivision',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.agency'),
        ),
        migrations.AddField(
            model_name='agencyleader',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.agency'),
        ),
        migrations.AlterField(
            model_name='report',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]