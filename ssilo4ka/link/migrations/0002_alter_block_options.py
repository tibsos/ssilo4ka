# Generated by Django 4.1.1 on 2022-10-10 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'ordering': ['updatedAt']},
        ),
    ]
