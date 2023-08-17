from django.db import models
from django.contrib.auth.models import User


class locationtable(models.Model):
    location = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class housenumber(models.Model):
    houseid = models.IntegerField()
    sellerid = models.IntegerField()
    location=models.CharField(max_length=200)
    image=models.ImageField(null=True, blank=True)
    bhk=models.CharField(max_length=50,null=True)
    sqfeet=models.CharField(max_length=200,null=True, blank=True)
    action=models.CharField(max_length=200,null=True, blank=True)
    others=models.CharField (max_length=200,null=True, blank=True)

class ghardhundousers(models.Model):
    name= models.CharField(max_length=100)
    dob= models.DateField()
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    cpassword= models.CharField(max_length=100)

class images(models.Model):
    image = models.ImageField(null=True, blank=True)


