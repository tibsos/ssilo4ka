# Generated by Django 4.1.1 on 2022-10-10 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Font',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.PositiveSmallIntegerField(verbose_name='Price [RUB]')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('mfa', models.BooleanField(default=False, verbose_name='Multi-factor Authentication')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=user.models.ua)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.TextField(blank=True, max_length=100, null=True)),
                ('logoHidden', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('background', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.background')),
                ('block', models.ManyToManyField(blank=True, related_name='profile_blocks', to='link.block')),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.button')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.category')),
                ('font', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.font')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.plan')),
                ('priorityLink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_priority_block', to='link.block')),
                ('redirectLink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_redirect_block', to='link.block')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.subcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]