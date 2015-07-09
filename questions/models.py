from django.db import models

class Question(models.Model):
	PHYSICS = 'P'
	CHEMISTRY = 'C'
	MATHS = 'M'
	Subject_Type_Choices = (
		(PHYSICS, 'Physics'),
		(CHEMISTRY, 'Chemistry'),
		(MATHS, 'Maths'),
	)
	subject = models.CharField(max_length=1, choices=Subject_Type_Choices)
	question_text = models.TextField()
	answer = models.CharField(max_length=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, related_name='choices')
	choice_text = models.CharField(max_length=200)

	def __unicode__(self):
		return ('%s -> %s' %(self.question, self.choice_text))
