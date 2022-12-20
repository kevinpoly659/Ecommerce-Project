from django.shortcuts import render,redirect
from userprofile.models import *
from mycart.models import *
from datetime import date
import datetime
from . models import *
import razorpay 
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from decimal import Decimal
from django.shortcuts import redirect, render,get_object_or_404,reverse


# Create your views here.
def order_cod(request,id):
    total=0
    address = Address.objects.get(id=id)
    cart_items =  cartItem.objects.filter(user=request.user)
    order_id_generated = str(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    if cart_items is None:
        return redirect('home')
    else:
        for ob in cart_items:
            total +=(ob.cartprice*ob.quantity)
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



def razor_success(request):
    total=0
    address = Address.objects.get(user=request.user)
    cart_items = cartItem.objects.filter(user=request.user)
    order_id_generated = str(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    if cart_items is None:
       return redirect('home')
    else:
        for ob in cart_items:
            total +=(ob.product.price*ob.quantity)
            
    
    dates = date.today() 
    payment_method = 'Razorpay'
    payment_id = str(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    pay=Payment(user=request.user,payment_method=payment_method,payment_id=payment_id,status='payment complete',created_at=dates)
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
    return redirect('account')


def paypal_payment(request,sum,val):
    host = request.get_host()
    amount = float(sum)
    amount *= 0.01368 
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': amount,
        # 'item_name': 'Order {}'.format(order.id),
        # 'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done',kwargs={'val':val})),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypal.html', {'form': form})


def payment_done(request,val):
    total=0
    address = Address.objects.get(id=val)
    cart_items = cartItem.objects.filter(user=request.user)
    order_id_generated = str(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    if cart_items is None:
       return redirect('home')
    else:
        for ob in cart_items:
            total +=(ob.product.price*ob.quantity)
            
    
    dates = date.today() 
    payment_method = 'Paypal'
    payment_id = str(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    pay=Payment(user=request.user,payment_method=payment_method,payment_id=payment_id,status='payment complete',created_at=dates)
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

def payment_cancelled(request):
    return redirect('account')