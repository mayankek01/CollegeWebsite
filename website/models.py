
from django.db import models

class Product(models.Model):
    img = models.ImageField(upload_to = 'pics')
    category = models.TextField()
    name = models.CharField(max_length=200)
    price = models.IntegerField()

class Teachingstaff(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact = models.IntegerField()
    qualification = models.CharField(max_length=100)
    readmore = models.URLField(max_length=100)

class nonTeachingstaff(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact = models.IntegerField()
    qualification = models.CharField(max_length=100)
    readmore = models.URLField(max_length=100)

class others(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact = models.IntegerField()
    qualification = models.CharField(max_length=100)
    readmore = models.URLField(max_length=100)

class collegenotices(models.Model):
    img = models.ImageField(upload_to='pics')
    date = models.DateField()
    topic = models.CharField(max_length=100)
    readmore = models.URLField(max_length=100)