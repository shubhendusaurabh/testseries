from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Exam(models.Model):
	name = models.CharField(max_length=100)
	abbr = models.CharField(max_length=10)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Subject(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Unit(models.Model):
	name = models.CharField(max_length=100)
	subject = models.ForeignKey(Subject)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Chapter(models.Model):
	name = models.CharField(max_length=100)
	unit = models.ForeignKey(Unit)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Question(models.Model):
	question_text = models.TextField()
	answer = models.CharField(max_length=2)
	hint = models.TextField(null=True, blank=True)
	chapter = models.ForeignKey(Chapter)
	image = models.ImageField(upload_to='static/img/questions', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.question_text

@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question, related_name='choices')
	choice_text = models.CharField(max_length=200)

	def __str__(self):
		return self.choice_text
