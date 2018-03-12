from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	def __str__(self):
		return self.user.username

class Project(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=200, default='Description')
	address = models.CharField(max_length=30, default='Address')
	status = models.CharField(max_length=30, default='Status')
	longitude = models.FloatField(default = 0)
	latitude = models.FloatField(default = 0)
	def __str__(self):
		return self.name

class Story(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE,)
	id = models.AutoField(primary_key=True)
	text = models.CharField(max_length=128, default='As ... I want ...')
	header = models.CharField(max_length=20, default='header')
	top = models.CharField(max_length=6, default='200px')
	left = models.CharField(max_length=6, default='50px')
	width = models.CharField(max_length=6, default='200px')
	heigth = models.CharField(max_length=6, default='100px')
	theme = models.CharField(max_length=30, default='sticky-note-green-theme')
	point = models.CharField(max_length=6, default='0')
	priority = models.CharField(max_length=12, default='High')
	def __str__(self):
		return self.header

class Sprint(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE,)
	story = models.ForeignKey(Story, on_delete=models.CASCADE,)
	id = models.AutoField(primary_key=True)
	iteration = models.CharField(max_length=3, default='0')
	startDate = models.CharField(max_length=20, default='1/1/2018')
	endDate = models.CharField(max_length=20, default='1/1/2018')
	releaseDate = models.CharField(max_length=20, default='1/1/2018')
	def __str__(self):
		return self.text