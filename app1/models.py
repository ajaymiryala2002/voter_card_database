from django.db import models

class Voter(models.Model):
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    photo = models.ImageField(upload_to='photos/')
