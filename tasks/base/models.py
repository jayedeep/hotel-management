from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class Restaurants(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    city=models.CharField(max_length=120)
    address=models.TextField(max_length=500)
    franchise=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Foods(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurants,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurants=models.ForeignKey(Restaurants,on_delete=models.CASCADE)
    foods=ArrayField(models.CharField(max_length=100))
    datetime=models.DateTimeField(default=timezone.now)
    table_no=models.CharField(max_length=20)
    totalbill=models.CharField(max_length=100)


    def __str__(self):
        return self.totalbill



