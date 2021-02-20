from django.db import models


# Create your models here.
class Person(models.Model):
    firstName = models.CharField(max_length=20, null=False)
    lastName = models.CharField(max_length=20)
    emailAddress = models.EmailField()
