from django.db import models

class Manager(models.Model):
	name = models.CharField(max_length=256, default='name')
	surname = models.CharField(max_length=256, default='surname')
	token = models.CharField(max_length=36, default='')

class Meeting(models.Model):
	manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)
	token = models.CharField(max_length=256, default='')
	time = models.DateTimeField()
	name = models.CharField(max_length=256, default='name')
	surname = models.CharField(max_length=256, default='surname')
	longitude = models.FloatField(default=0.0)
	latitude = models.FloatField(default=0.0)
	address = models.CharField(max_length=256, default='')