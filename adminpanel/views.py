from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from userprofile.models import Account
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from catagory . models import catagories, brands, sub_catagories
from products . models import products, coupon, productoffer,catagoryoffer
from django.views.decorators.cache import cache_control
from orders .models import *
from datetime import datetime,date
import datetime
import _strptime
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from .forms import Imageform
from django.http import JsonResponse


# Create your views here.
def admin_login(request):
    if 'username' in request.session:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_superuser:
                login(request,user)
                request.session['username'] = username
                messages.info(request, 'Logged in Successfully')
                currentuser = request.user
                return render(request, 'ad/index-admin.html', {'currentuser':currentuser})
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login')
        else:  
            return render(request, 'ad/page-account-login.html')





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    sumorder=0
    sumcod=0
    sumrazor=0
    sumppal=0
    ob=products.objects.all()
    ob2=Order.objects.all()
    countorder = Order.objects.all().count()
    countprod = products.objects.all().count()
    countcat = catagories.objects.all().count()
    cod = Payment.objects.filter(payment_method='COD')
    ppal = Payment.objects.filter(payment_method='Paypal')
    rz = Payment.objects.filter(payment_method='Razorpay')
    catmen = OrderProduct.objects.filter(product__catagory__catagory_name= "Men's Fashion").count()
    catwomen = OrderProduct.objects.filter(product__catagory__catagory_name= "Women's Fashion").count()
    catkid = OrderProduct.objects.filter(product__catagory__catagory_name= "Kids").count()
    countcod = cod.count()
    countppal = ppal.count()
    countrz = rz.count()
    
    for obj in ob2:
        for obj2 in cod:
            if obj.payment == obj2:
                sumcod += obj.ordertotal
    for obj in ob2:
        for obj2 in ppal:
            if obj.payment == obj2:
                sumppal += obj.ordertotal
      
    for obj in ob2:
        for obj2 in rz:
            if obj.payment == obj2:
                sumrazor += obj.ordertotal      
            
            
    
    for obj in ob2:
        sumorder+=obj.ordertotal
        
    return render(request, 'ad\index-admin.html',{'orders':countorder, 'products':countprod, 'ordertotal':sumorder, 'categories':countcat,'Cod':countcod, 'ppal':countppal, 'razor':countrz,'sumcod':sumcod,'sumppal':sumppal,'sumrazor':sumrazor,
                                                  'catmen':catmen, 'catwomen': catwomen,'catkid':catkid})


@login_required
def admin_logout(request):
    request.session.flush()
    messages.success(request, "Logged Out Successfully")
    return redirect('login')

def admin_users(request, *args, **kwargs):
    obj = Account.objects.all().order_by('id')
    return render(request, 'ad\page-users.html', {'users':obj})

def block_user(request, id):
    x=Account.objects.get(id = id)
    x.is_active = False
    x.save()
    return redirect('adminusers')
    
def unblock_user(request, id):
    x=Account.objects.get(id = id)
    x.is_active = True
    x.save()
    return redirect('adminusers')

def admin_products(request):
    obj = products.objects.all()
    obj2 = brands.objects.all()
    return render(request, 'ad\page-products.html', {'products':obj, 'brands':obj2})

def admin_addproduct(request):
    obj4 = catagories.objects.all()
    obj5 = brands.objects.all()
    obj6 = sub_catagories.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('desc')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        sizeS = request.POST.get('sizeS')
        sizeM = request.POST.get('sizeM')
        sizeL = request.POST.get('sizeL')
        sizeXL = request.POST.get('sizeXL')
        sizeXXL = request.POST.get('sizeXXL')
        catagory = request.POST.get('catagory')
        brand = request.POST.get('brand')
        sub_cat = request.POST.get('sub_catagory')
        catagory_instance = catagories.objects.get(catagory_name=catagory)
        brand_instance = brands.objects.get(brand_name=brand)
        sub_cat_instance = sub_catagories.objects.get(subcatagory_name=sub_cat)
        prod = products(name=name,description=description,price=price,catagory=catagory_instance,sizeS=sizeS,sizeM=sizeM,sizeL=sizeL,sizeXL=sizeXL,sizeXXL=sizeXXL,brand=brand_instance,sub_catagory=sub_cat_instance,image=image,image2=image2,image3=image3,image4=image4)
        prod.save()
        return redirect('adminproducts')
        
        
    return render(request, 'ad\page-add-product.html', {'cat':obj4,'brnd':obj5,'sub':obj6})

def main_view(request):
    form = Imageform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'works'})
    context = {'form': form}
    return render(request, 'ad/imagecrop.html', context)



def admin_editproduct(request, id):
    inst = products.objects.get(id=id)
    obj4 = catagories.objects.all()
    obj5 = brands.objects.all()
    obj6 = sub_catagories.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('desc')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        size = request.POST.get('size')
        catagory = request.POST.get('catagory')
        brand = request.POST.get('brand')
        sub_cat = request.POST.get('sub_catagory')
        catagory_instance = catagories.objects.get(catagory_name=catagory)
        brand_instance = brands.objects.get(brand_name=brand)
        sub_cat_instance = sub_catagories.objects.get(subcatagory_name=sub_cat)
        
        
        inst.name = name
        inst.description = description
        inst.price = price
        print("size=",size)
        inst.size = size
        inst.catagory = catagory_instance
        inst.brand = brand_instance
        inst.sub_catagory = sub_cat_instance
        
        
        if image != None:
            inst.image = image
        if image2 != None:
            inst.image2 = image2
        if image3 != None:
            image3 = image3
        if image4 != None:
            inst.image4 = image4
        inst.save()
    
    return render(request, 'ad\page-edit-product.html', {'edit':inst,'cat':obj4,'brnd':obj5,'sub':obj6})



def admin_deleteproduct(request, id):
    products.objects.get(id=id).delete()
    return redirect('adminproducts')

def admin_catagory(request):
    inst = catagories.objects.all()
    inst2 = sub_catagories.objects.all()
    return render(request, 'ad\page-catagory.html', {'cat':inst,'sub':inst2})

def admin_addcatagory(request):
    inst = catagories.objects.all()
    if request.method == 'POST':
        name = request.POST.get('catagory_name')
        cat = catagories(catagory_name=name)
        cat.save()
        return redirect('admincatagory')

    return render(request, 'ad\page-add-catagory.html', {'cat':inst})

def admin_addsubcatagory(request):
    
    inst = catagories.objects.all()
    if request.method == 'POST':
        catname = request.POST.get('catagory')
        cat = catagories.objects.get(catagory_name=catname)
        subname = request.POST.get('subcatagory_name')
        try:
            subcat = sub_catagories.objects.get(catagories = cat, subcatagory_name=subname)
            messages.info(request,"Subcategory Already Exists")
        except:
            subcat = sub_catagories(catagories = cat, subcatagory_name=subname)
            subcat.save()
            return redirect('admincatagory')
    return render(request, 'ad\page-add-subcatagory.html', {'cat':inst})


def admin_editcatagory(request, id):
    inst = catagories.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('catagory_name')
        inst.catagory_name = name
        inst.save()
    return render(request, 'ad\page-edit-catagory.html', {'cat':inst})
     
def admin_editsubcatagory(request, id):
    inst = sub_catagories.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('subcatagory_name')
        inst.subcatagory_name = name
        inst.save()
    return render(request, 'ad/page-edit-subcatagory.html', {'cat':inst})
   
def delete_catagory(request, id):
    catagories.objects.get(id=id).delete()
    return redirect('admincatagory')
        
        
def admin_orders(request):
    
    orders = Order.objects.all()
    return render(request, 'ad/page-orders.html',{'orders':orders})


def admin_order_details(request, id):
    orders = Order.objects.get(id=id)
    order_details = OrderProduct.objects.filter(order=orders)
    return render(request,'ad/page-orders-detail.html',{'orders':orders,'order_details':order_details})


def order_status_change(request, id):
    orders = Order.objects.get(id=id)
    if request.method == 'POST':
        status = request.POST.get('status')
        orders.status = status
        orders.save()
    return render(request, 'ad/page-orders-detail.html',{'orders':orders})


def sales_report(request):
    salesreport = Order.objects.all().order_by('id')
    
    
    return render(request, 'ad/page-sales.html')

def monthly_sales(request):
    if request.method=='POST':
        dates= request.POST.get('date')
        frm = datetime.datetime.strptime(dates, '%B').month
        fromdate = int(frm)
        try:
            fm = [2022,frm,1]
            todt = [2022,frm,30]
            salesreport = Order.objects.filter(date__gte = datetime.date(fm[0],fm[1],fm[2]),date__lte=datetime.date(todt[0],todt[1],todt[2])).order_by("-id")
        except:
            fm = [2022,frm,1]
            todt = [2022,frm,28]
            salesreport = Order.objects.filter(date__gte = datetime.date(fm[0],fm[1],fm[2]),date__lte=datetime.date(todt[0],todt[1],todt[2])).order_by("-id")
    if len(salesreport)>0:
        context = {
            'salesreport':salesreport,
        }
        return render(request,'ad/page-sales.html',context)

    else:
        messages.error(request,"No Orders")
        return render(request,'ad/page-sales.html')
    


def yearly_sales(request):
    if request.method=='POST':
        dates= request.POST.get('date')
        frm = int(dates)
        try:
            fm = [frm,1,1]
            todt = [frm,12,30]
            salesreport = Order.objects.filter(date__gte = datetime.date(fm[0],fm[1],fm[2]),date__lte=datetime.date(todt[0],todt[1],todt[2])).order_by("-id")
        except:
            fm = [2022,frm,1]
            todt = [2022,frm,28]
            salesreport = Order.objects.filter(date__gte = datetime.date(fm[0],fm[1],fm[2]),date__lte=datetime.date(todt[0],todt[1],todt[2])).order_by("-id")
    if len(salesreport)>0:
        context = {
            'yearlysalesreport':salesreport,
        }
        return render(request,'ad/page-sales.html',context)

    else:
        messages.error(request,"No Orders")
        return render(request,'ad/page-sales.html')
    
    
    
def admin_coupon(request):
    inst = coupon.objects.all()
    return render(request, 'ad/page-coupon.html', {'coupon':inst})




def add_coupon(request):
    
    if request.method == 'POST':
        code = request.POST.get('coupon_code')
        discount = request.POST.get('discount')
        inst = coupon(code=code,discount=discount)
        inst.save()
        return redirect('coupon')
    return render(request, 'ad/page-add-coupon.html')


def admin_offers(request):
    inst = productoffer.objects.all()
    inst2= catagoryoffer.objects.all()
    return render(request,'ad/page-offers.html',{'prodoffers':inst,'categoryoffers':inst2})



def add_product_offer(request):
    inst = products.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('product_name')
        product = products.objects.get(name = name)
        offer = request.POST.get('offer')
        inst2 = productoffer(product=product, offer=offer)
        inst2.save()
        return redirect('offers')
    return render(request,'ad/page-add-product-offer.html',{'products':inst})

def delete_product_offer(request,id):
    offer = productoffer.objects.get(id=id)
    offer.delete()
    return redirect('offers')


def add_catagory_offer(request):
    inst = catagories.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('catagory_name')
        catagory = catagories.objects.get(catagory_name=name)
        offer = request.POST.get('offer')
        inst2 = catagoryoffer(catagory=catagory,offer=offer)
        inst2.save()
        return redirect('offers')
    return render(request,'ad/page-add-catagory-offer.html',{'catagory':inst})

def delete_catagory_offer(request, id):
    offer = catagoryoffer.objects.get(id=id)
    offer.delete()
    return redirect('offers')