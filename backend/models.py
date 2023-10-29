from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=5)
    mid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    point = models.IntegerField()

    def __str__(self):
        return self.name

class Stores(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Inquiry(models.Model):
    mid = models.CharField(max_length=100)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.mid