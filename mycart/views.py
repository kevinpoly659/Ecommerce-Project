from django.shortcuts import render
from django.contrib import messages
from products . models import products,coupon
from . models import cart, cartItem
from userprofile.views import *
from userprofile.models import Guest
import razorpay

# Create your views here.
def addcart(request, id):
    if request.method == "POST":
        qty = int(request.POST.get('qty'))
        size = request.POST.get('size')
    product = products.objects.get(id=id)
    try:
        try:
            cart_item = cartItem.objects.get(product = product, user = request.user, size = size)
            cart_item.quantity += qty
            if product.price != product.discountprice:
                cart_item.cartprice += (cart_item.product.discountprice*qty)
            else:
                cart_item.cartprice += (cart_item.product.price*qty)
            cart_item.save()
        except:
            if product.price != product.discountprice:
                print(product.discountprice)
                cartprice = product.discountprice*qty
            else:
                cartprice = product.price*qty
            cartitem = cartItem.objects.create(product = product, quantity = qty , cartprice=cartprice , user = request.user , size = size)
            cartitem.save()
    except:
        guest = Guest.objects.get(name='guest')
        try:
            cart_item = cartItem.objects.get(product = product, guest = guest.uid, size = size)
            cart_item.quantity += qty
            if product.price != product.discountprice:
                cart_item.cartprice += (cart_item.product.discountprice*qty)
            else:
                cart_item.cartprice += (cart_item.product.price*qty)
            cart_item.save()
        except:
            if product.price != product.discountprice:
                cartprice = product.discountprice*qty
            else:
                cartprice = product.price*qty
            cartitem = cartItem.objects.create(product = product, quantity = qty , cartprice=cartprice , guest = guest.uid , size = size)
            cartitem.save()
    return redirect('viewprod',product.id)

def viewcart(request, disc, subtotal=0):
    try:
        cart_item = cartItem.objects.filter(user=request.user)
    except:
        guest = Guest.objects.get(name='guest')
        cart_item = cartItem.objects.filter(guest=guest.uid) 
    product = products.objects.all()
    for ob in product:
        for ob2 in cart_item:
            if ob2.product == ob:
                subtotal += ob2.cartprice     
    orginal = subtotal
    if disc!=0:
        subtotal -= disc
    return render(request,'cart/cart.html',{'cart':cart_item,'prod':product, 'sum':subtotal,'discount':disc,'orginal':orginal})


def apply_coupon(request,cod):
    print(cod)
    
    inst = coupon.objects.get(code = cod)
    dis=inst.discount
    return redirect('viewcart',dis)



def deletecart(request, id):
    if 'username' in request.session:
        cartItem.objects.get(id=id,user=request.user).delete()
    else:
        guest = Guest.objects.get(name='guest')
        cartItem.objects.get(id=id,guest=guest.uid).delete()
    return redirect('viewcart',0)

def clearcart(request):
    if 'username' in request.session:
        cartItem.objects.filter(user=request.user).delete()
    else:
        guest = Guest.objects.get(name='guest')
        cartItem.objects.filter(guest=guest.uid).delete()
    return redirect('viewcart',0)

def checkout(request, sum):
    try:
        cart_item = cartItem.objects.filter(user=request.user)
    except:
        cart_item = cartItem.objects.filter(guest=(Guest.objects.get(name='guest')).uid)
    product = products.objects.all()
    amount = float(sum)*100
        
    try:
        address = Address.objects.filter(user=request.user)
    except: 
        address = None
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