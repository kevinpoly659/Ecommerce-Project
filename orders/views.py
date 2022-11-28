from django.shortcuts import render,redirect
from userprofile.models import *
from mycart.models import *
from datetime import date
import datetime
from . models import *
import razorpay 


# Create your views here.
def order_cod(request):
    total=0
    address = Address.objects.get(user=request.user)
    cart_items =  cartItem.objects.filter(user=request.user)
    order_id_generated = str(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    if cart_items is None:
        return redirect('home')
    else:
        for ob in cart_items:
            total +=(ob.product.price*ob.quantity)
    dates = date.today() 
    payment_method = 'COD'
    pay = Payment(user=request.user, payment_method=payment_method, status='pending', created_at=dates)
    pay.save()
    
    orders = Order(user=request.user, address=address, ordertotal=total, orderid=order_id_generated, date=dates, payment=pay)
    orders.save()
    
    for ob in cart_items:
        order_products = OrderProduct(order=orders,user=request.user)
        product = products.objects.get(id=ob.product.id)
        order_products.product = ob.product
        order_products.quantity = ob.quantity
        order_products.price = ob.cartprice
        product.save()
        order_products.save()
    
    
    for ob in cart_items:
        ob.delete()
        
    return redirect('account')



def order_razorpay(request):
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(
            auth = ('rzp_live_QPrFX9xDqw14Qe','LV6QVWzm9hIXyhTn0VM0UVMP')
        )
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})