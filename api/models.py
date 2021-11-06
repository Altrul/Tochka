from django.db import models

class Manager(models.Model):
	name = models.CharField(max_length=256, default='name')
	surname = models.CharField(max_length=256, default='surname')
	phone = models.CharField(max_length=32, default='')
	token = models.CharField(max_length=36, default='')
	status = models.BooleanField(default=True)
	distance = models.FloatField(default=0)
	meeting_count = models.IntegerField(default=0)

class Meeting(models.Model):
	manager_token = models.CharField(max_length=36, default='')
	token = models.CharField(max_length=256, default='')
	time = models.DateTimeField()
	name = models.CharField(max_length=256, default='name')
	surname = models.CharField(max_length=256, default='surname')
	longitude = models.FloatField(default=0.0)
	latitude = models.FloatField(default=0.0)
	address = models.CharField(max_length=256, default='')
	phone = models.CharField(max_length=32, default='')