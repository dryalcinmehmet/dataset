# Generated by Django 2.2 on 2019-05-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20190517_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customprofile',
            name='avatar',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
