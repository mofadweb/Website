# Generated by Django 3.2 on 2021-04-20 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0007_auto_20210420_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.institution'),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='year_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.yeargroup'),
        ),
    ]
