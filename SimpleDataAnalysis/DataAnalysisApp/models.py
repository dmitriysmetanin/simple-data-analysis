from django.db import models

class Feedback(models.Model):
    organization = models.CharField(max_length=255)
    problem = models.TextField()
    contact = models.CharField(max_length=255)
    status = models.IntegerField(default=0)


