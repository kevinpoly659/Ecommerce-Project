from django.shortcuts import render
from products . models import products
from . models import cart, cartItem
from userprofile.views import *

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

def viewcart(request, subtotal=0):
    cart_item = cartItem.objects.filter(user=request.user)
    product = products.objects.all()
    for ob in product:
        for ob2 in cart_item:
            if ob2.product == ob:
                subtotal += ob2.cartprice       
    return render(request,'cart/cart.html',{'cart':cart_item,'prod':product, 'sum':subtotal})

def deletecart(request, id):
    cartItem.objects.get(id=id).delete()
    return redirect('viewcart')

def clearcart(request):
    cartItem.objects.all().delete()
    return redirect('viewcart')

def checkout(request, sum):
    cart_item = cartItem.objects.filter(user=request.user)
    product = products.objects.all()
    try:
        address = Address.objects.get(user=request.user)
    except: 
        return redirect('addaddress')
    return render(request, 'cart/checkout.html',{'cart':cart_item, 'prod':product,'sum':sum,'address':address})