# Generated by Django 4.1.1 on 2022-10-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
