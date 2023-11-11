from django.db import models

# Create your models here.

    

class products(models.Model):
    product_id = models.IntegerField( unique=True,blank=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class pro_details(models.Model):
    product_id = models.IntegerField( unique=True,blank=False,primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

