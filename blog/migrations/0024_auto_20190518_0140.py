# Generated by Django 2.2.1 on 2019-05-17 22:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190518_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 17, 22, 40, 4, 273932, tzinfo=utc)),
        ),
    ]
