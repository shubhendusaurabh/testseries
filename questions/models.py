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
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)