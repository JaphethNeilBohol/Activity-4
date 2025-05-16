from django.db import models

class Product(models.Model):
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    manufacture_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.product
# Create your models here.
