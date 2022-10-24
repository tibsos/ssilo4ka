# Generated by Django 4.1.1 on 2022-10-24 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
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
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(max_length=254)),
                ('avatar', models.ImageField(upload_to=user.models.ua)),
                ('title', models.CharField(default='', max_length=30)),
                ('bio', models.TextField(default='', max_length=100)),
                ('mfa', models.BooleanField(default=False, verbose_name='Multi-factor Authentication')),
                ('ip', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('logoHidden', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activity', models.ManyToManyField(blank=True, to='app.pageactivity')),
                ('background', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.background')),
                ('block', models.ManyToManyField(blank=True, related_name='profile_blocks', to='app.block')),
                ('button', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.button')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.category')),
                ('font', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.font')),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.plan')),
                ('priority_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_priority_block', to='app.block')),
                ('redirect_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_redirect_block', to='app.block')),
                ('statistics', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='app.pagestatistics')),
                ('subCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.subcategory')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.theme')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='subCategory',
            field=models.ManyToManyField(blank=True, to='user.subcategory'),
        ),
    ]
