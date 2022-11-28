from django.db import models
from userprofile .models import Account
from products .models import products


# Create your models here.
class cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
class cartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    cart = models.ForeignKey(cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    cartprice = models.FloatField(null=True)
    size = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product.name