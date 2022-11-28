from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products . models import products
from catagory .models import catagories, brands, sub_catagories
from userprofile .models import Account

def home(request):
    obj= products.objects.all()[:9]
    obj3 = catagories.objects.all()
    obj4 = sub_catagories.objects.all()
    obj2 = products.objects.order_by('-added_on')[:9]
    return render(request, 'index.html', {'feature':obj, 'new':obj2, 'cat':obj3, 'sub':obj4})

def view_prod(request, id):
    obj3 = products.objects.get(id=id)
    return render(request, 'product-view.html', {'view':obj3})