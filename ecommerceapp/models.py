from django.db import models
# Create your models here.
class ProductData(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    discount_price=models.IntegerField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=300)

    def  __str__(self):
        return self.title
    
class OrderData(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
 
    