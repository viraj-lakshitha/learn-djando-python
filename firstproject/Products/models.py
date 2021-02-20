from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100) # It is mandatory to have the max_digits and decimal_places
    summary = models.TextField(null=False)
