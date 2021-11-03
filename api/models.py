from django.db import models

class Manager(models.Model):
	name = models.CharField(max_length=256, default='name')
	surname = models.CharField(max_length=256, default='surname')
	token = models.CharField(max_length=256, default='')

class Meeting(models.Model):
	# manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)
	time = models.DateTimeField()
	name = models.CharField(max_length=256, default='name')
	surname = models.CharField(max_length=256, default='surname')