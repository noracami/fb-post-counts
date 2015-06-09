# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageitem',
            name='picture_url',
            field=models.CharField(max_length=250, verbose_name='大頭貼', default='hi'),
            preserve_default=False,
        ),
    ]
