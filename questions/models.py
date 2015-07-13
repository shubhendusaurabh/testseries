from django.db import models

class Exam(models.Model):
	name = models.CharField(max_length=100)
	abbr = models.CharField(max_length=10)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Unit(models.Model):
	name = models.CharField(max_length=100)
	subject = models.ForeignKey(Subject)

	def __unicode__(self):
		return self.name

class Chapter(models.Model):
	name = models.CharField(max_length=100)
	unit = models.ForeignKey(Unit)

	def __unicode__(self):
		return self.name

class Question(models.Model):
	question_text = models.TextField()
	answer = models.CharField(max_length=2)
	chapter = models.ForeignKey(Chapter)
	image = models.ImageField(upload_to='static/img/questions', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, related_name='choices')
	choice_text = models.CharField(max_length=200)

	def __unicode__(self):
		return ('%s -> %s' %(self.question, self.choice_text))
