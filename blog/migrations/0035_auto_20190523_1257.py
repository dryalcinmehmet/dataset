# Generated by Django 2.2.1 on 2019-05-23 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20190522_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='qa',
            name='edit_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='qanswer',
            name='edit_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
