# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('abbr', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(to='questions.Subject')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='subject',
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(related_name='choices', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='unit',
            field=models.ForeignKey(to='questions.Unit'),
        ),
        migrations.AddField(
            model_name='question',
            name='chapter',
            field=models.ForeignKey(to='questions.Chapter'),
            preserve_default=False,
        ),
    ]
