# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20150724_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='hint',
            field=models.TextField(blank=True, null=True),
        ),
    ]
