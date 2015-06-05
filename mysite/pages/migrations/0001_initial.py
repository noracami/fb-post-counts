# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名稱')),
                ('fb_id', models.IntegerField(verbose_name='Facebook 專頁編號')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='加入時間')),
                ('last_access_time', models.DateTimeField(verbose_name='上次存取時間')),
                ('last_like_count', models.IntegerField(verbose_name='上次粉絲人數')),
                ('notes', models.TextField(blank=True, default='', verbose_name='備註')),
            ],
            options={
                'verbose_name': 'Facebook 專頁',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('account', models.CharField(max_length=30, verbose_name='帳號')),
                ('name', models.CharField(max_length=20, verbose_name='名稱')),
            ],
            options={
                'verbose_name': '使用者',
            },
        ),
        migrations.AddField(
            model_name='pageitem',
            name='user',
            field=models.ForeignKey(to='pages.User', related_name='page_items'),
        ),
    ]
