from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from catagory . models import catagories, brands, sub_catagories
from products . models import products
from django.views.decorators.cache import cache_control

# Create your views here.


def product(request, id1, id2):
    if id1 == "None":
        inst = sub_catagories.objects.get(subcatagory_name=id2)
        ob1 = products.objects.filter(sub_catagory=inst)

    elif id2 == "None":
        inst = catagories.objects.get(catagory_name=id1)
        ob1 = products.objects.filter(catagory=inst)
        
    return render(request,'products.html',{'cntx': ob1})