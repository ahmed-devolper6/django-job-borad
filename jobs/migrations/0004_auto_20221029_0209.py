# Generated by Django 3.2 on 2022-10-29 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0003_jobs_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='user',
        ),
        migrations.AddField(
            model_name='jobs',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
