# Generated by Django 2.2 on 2019-05-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_remove_customprofile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customprofile',
            name='avatar',
            field=models.ImageField(upload_to=''),
        ),
    ]
