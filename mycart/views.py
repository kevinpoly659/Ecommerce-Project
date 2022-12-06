from django.shortcuts import render
from django.contrib import messages
from products . models import products,coupon
from . models import cart, cartItem
from userprofile.views import *
import razorpay

# Create your views here.
def addcart(request, id):
    if request.method == "POST":
        qty = int(request.POST.get('qty'))
        size = request.POST.get('size')
    product = products.objects.get(id=id)
    try:
        cart_item = cartItem.objects.get(product = product, user = request.user, size = size)
        cart_item.quantity += qty
        cart_item.cartprice += (cart_item.product.price*qty)
        cart_item.save()
    except:
        cartprice = product.price*qty
        cartitem = cartItem.objects.create(product = product, quantity = qty , cartprice=cartprice , user = request.user , size = size)
        cartitem.save()
    return redirect('viewprod',product.id)

def viewcart(request, disc, subtotal=0):
    cart_item = cartItem.objects.filter(user=request.user)
    product = products.objects.all()
    for ob in product:
        for ob2 in cart_item:
            if ob2.product == ob:
                subtotal += ob2.cartprice     
    if disc!=0:
        subtotal -= disc
    return render(request,'cart/cart.html',{'cart':cart_item,'prod':product, 'sum':subtotal})


def apply_coupon(request,cod):
    print(cod)
    
    inst = coupon.objects.get(code = cod)
    dis=inst.discount
    return redirect('viewcart',dis)



def deletecart(request, id):
    cartItem.objects.get(id=id,user=request.user).delete()
    return redirect('viewcart',0)

def clearcart(request):
    cartItem.objects.filter(user=request.user).delete()
    return redirect('viewcart',0)

def checkout(request, sum):
    cart_item = cartItem.objects.filter(user=request.user)
    product = products.objects.all()
    amount = float(sum)*100
        
    try:
        address = Address.objects.filter(user=request.user)
    except: 
        return redirect('addaddress')
    client = razorpay.Client(
            auth = ('rzp_live_QPrFX9xDqw14Qe','LV6QVWzm9hIXyhTn0VM0UVMP')
        )
    global payments
    payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    payment_id = payment["id"]
    return render(request, 'cart/checkout.html',{'cart':cart_item, 'prod':product,'sum':sum,'address':address,'amount':amount})


    

def add_quantity(request,id,):
    cartitem = cartItem.objects.get(id=id,user=request.user)
    cartitem.quantity += 1
    cartitem.cartprice += cartitem.product.price
    cartitem.save()
    return redirect('viewcart',0)

def down_quantity(request,id):
    cartitem = cartItem.objects.get(id=id,user=request.user)
    if cartitem.quantity > 1:
        cartitem.quantity -= 1
        cartitem.cartprice -= cartitem.product.price
        cartitem.save()
    else:
        cartItem.objects.get(id=id,user=request.user).delete() 

    return redirect('viewcart',0)