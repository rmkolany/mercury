# Generated by Django 3.2.5 on 2023-03-14 18:53

import apps.accounts.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of Mercury Site', max_length=256)),
                ('slug', models.CharField(help_text='Subdomain', max_length=256, unique=True)),
                ('domain', models.CharField(blank=True, default='runmercury.com', help_text='Domain address', max_length=256, null=True)),
                ('custom_domain', models.CharField(blank=True, help_text='Custom domain address', max_length=256, null=True, unique=True)),
                ('share', models.CharField(choices=[('PUBLIC', 'Anyone can access notebooks and execute'), ('PRIVATE', 'Only selected users have access to notebooks')], default='PUBLIC', max_length=32)),
                ('status', models.CharField(default='Created', max_length=32)),
                ('info', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', apps.accounts.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', apps.accounts.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('token', models.TextField()),
                ('created_at', apps.accounts.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hosted_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.site')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rights', models.CharField(choices=[('VIEW', 'View and execute notebooks'), ('EDIT', 'Edit and view site, files and execute notebooks')], default='VIEW', help_text='Rights for user', max_length=32)),
                ('created_at', apps.accounts.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', apps.accounts.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='accounts.site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=128)),
                ('invited', models.CharField(max_length=256)),
                ('created_at', apps.accounts.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
