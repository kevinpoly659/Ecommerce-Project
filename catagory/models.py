from django.db import models

# Create your models here.
class catagories(models.Model):
    catagory_name = models.CharField(max_length=200, unique=True)    

    def __str__(self):
        return self.catagory_name
class sub_catagories(models.Model):
    catagories = models.ForeignKey(catagories, on_delete=models.CASCADE)
    subcatagory_name = models.CharField(max_length=200)
    def __str__(self):
        return self.subcatagory_name

class brands(models.Model):
    brand_name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.brand_name