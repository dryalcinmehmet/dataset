# Generated by Django 2.2 on 2019-05-16 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='static/img/avatar/avatar.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(db_index=True, default='', max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='grade',
            field=models.CharField(choices=[('Aday', 'Aday'), ('Çırak', 'Çırak'), ('Kalfa', 'Kalfa'), ('Usta', 'Usta'), ('Büyük Usta', 'Büyük Usta')], default='Aday', max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='talents',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='uni',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
