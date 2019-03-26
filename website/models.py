from django.db import models
from django.utils import timezone
from django.urls import reverse

class Contact(models.Model):
	name= models.CharField(max_length=75)
	email = models.EmailField()
	message = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)



	def __str__(self):
		return self.email

class Questions(models.Model):
	name = models.CharField(max_length=125)
	level = models.CharField(max_length=75)
	semester = models.CharField(max_length=75)
	faculty = models.CharField(max_length=75)
	date_posted = models.DateTimeField(default=timezone.now)
	file = models.FileField()

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.name
