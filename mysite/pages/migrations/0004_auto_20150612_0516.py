# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150612_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageitem',
            name='fb_id',
            field=models.BigIntegerField(verbose_name='Facebook 專頁編號'),
        ),
    ]
