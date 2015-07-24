# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hint',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(upload_to='static/img/questions', blank=True, null=True),
        ),
    ]
