from django.db import models

# Create your models here.
class men(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField

class men_detail(models.Model):
    catagory = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price_s = models.DecimalField(max_digits=5, decimal_places=2)
    price_m = models.DecimalField(max_digits=5, decimal_places=2)
    price_l = models.DecimalField(max_digits=5, decimal_places=2)
    price_xl = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(blank=True, null=True)
    
class women(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField

class women_detail(models.Model):
    catagory = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price_s = models.DecimalField(max_digits=5, decimal_places=2)
    price_m = models.DecimalField(max_digits=5, decimal_places=2)
    price_l = models.DecimalField(max_digits=5, decimal_places=2)
    price_xl = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(blank=True, null=True)

class ad(models.Model):
    picture = models.ImageField(blank=True, null=True)
