# Generated by Django 4.1.1 on 2022-10-13 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_avatar_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='avatars_profile', to='user.profile'),
            preserve_default=False,
        ),
    ]
