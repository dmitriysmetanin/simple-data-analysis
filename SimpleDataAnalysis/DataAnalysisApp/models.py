from django.db import models

class Feedback(models.Model):
    organization = models.CharField(max_length=255)
    problem = models.TextField()
    contact = models.CharField(max_length=255)
    status = models.IntegerField(default=0)

class ComparisonModelFeature(models.Model):
    name = models.CharField(max_length=255)
    data_delimiter = models.CharField(max_length=16)
    data = models.TextField()

class ComparisonModel(models.Model):
    name = models.CharField(max_length=255)
    features = models.ManyToOneRel(ComparisonModelFeature)