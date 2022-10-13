# Generated by Django 4.1.1 on 2022-10-12 15:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_alter_link_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]