# Generated by Django 3.2.3 on 2021-05-23 08:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_post_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favourite',
        ),
        migrations.AddField(
            model_name='post',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]
