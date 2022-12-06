from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from catagory . models import catagories, brands, sub_catagories
from datetime import datetime    


size_choices = (("S","S"),
               ("M","M"),
               ("L","L"),
               ("XL","XL"),
               ("XXL","XXL"))


# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    size = models.CharField(max_length=200, default="S")
    sizeS = models.IntegerField(validators=[MinValueValidator(0)], blank=True, default=100)
    sizeM = models.IntegerField(validators=[MinValueValidator(0)], blank=True, default=100)
    sizeL = models.IntegerField(validators=[MinValueValidator(0)], blank=True, default=100)
    sizeXL = models.IntegerField(validators=[MinValueValidator(0)], blank=True, default=100)
    sizeXXL = models.IntegerField(validators=[MinValueValidator(0)], blank=True, default=100)
    image = models.ImageField(upload_to="images/")
    image2 = models.ImageField(upload_to="images/")
    image3 = models.ImageField(upload_to="images/")
    image4 = models.ImageField(upload_to="images/")
    added_on = models.DateTimeField(auto_now_add=True, blank=True)
    is_available = models.BooleanField(default=True)
    catagory = models.ForeignKey(catagories, on_delete=models.CASCADE)
    sub_catagory = models.ForeignKey(sub_catagories, on_delete=models.CASCADE)
    brand = models.ForeignKey(brands, on_delete=models.CASCADE)




class coupon(models.Model):
    code = models.CharField(max_length=200,unique=True)
    discount = models.IntegerField(validators=[MinValueValidator(0)])
    def __str__(self):
        return self.code
    
    
class productoffer(models.Model):
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    offer = models.IntegerField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product.name
    
class catagoryoffer(models.Model):
    catagory = models.ForeignKey(catagories, on_delete=models.CASCADE)
    offer = models.IntegerField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.catagory.catagory_name
    