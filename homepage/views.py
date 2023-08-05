from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products . models import products
from catagory .models import catagories, brands, sub_catagories
from userprofile .models import Account,Guest

def home(request):
    # if 'username' not in request.session:
    #     try:
    #         guest = Guest.objects.create(name='guest')
    #         guest.save()
    #     except:
    #         guest = Guest.objects.create(name='guest')
    #         guest.save()
    obj= products.objects.all()[:9]
    obj3 = catagories.objects.order_by('catagory_name')
    obj4 = sub_catagories.objects.order_by('subcatagory_name')
    obj2 = products.objects.order_by('-added_on')[:9]
    return render(request, 'index.html', {'feature':obj, 'new':obj2, 'cat':obj3, 'sub':obj4})

def view_prod(request, id):
    obj3 = products.objects.get(id=id)
    return render(request, 'product-view.html', {'view':obj3})
