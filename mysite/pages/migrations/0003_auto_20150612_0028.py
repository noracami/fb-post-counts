# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0002_pageitem_picture_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageitem',
            name='user',
        ),
        migrations.AddField(
            model_name='pageitem',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_page_items', null=True),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='last_access_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上次存取時間'),
        ),
    ]
