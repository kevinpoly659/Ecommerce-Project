from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from catagory . models import catagories, brands, sub_catagories
from products . models import products, productoffer,catagoryoffer
from django.views.decorators.cache import cache_control
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def product(request, id1, id2):
    if id1 == "None":
        inst = sub_catagories.objects.get(subcatagory_name=id2)
        ob1 = products.objects.filter(sub_catagory=inst)
        inst2 = None
        

    elif id2 == "None":
        inst = catagories.objects.get(catagory_name=id1)
        inst2 = sub_catagories.objects.filter(catagories=inst)
        ob1 = products.objects.filter(catagory=inst)
        try:
            coffer=catagoryoffer.objects.get(category=inst)
            cof = coffer.offer
        except:
            print("NNNNNNN")     
        for ob in ob1:
            try:
                poffer = productoffer.objects.get(product = ob)
                pof = poffer.offer
                if poffer:
                    ob.discountprice = int(ob.price-(ob.price*(pof/100))) 
                    ob.save()   
                if poffer and coffer:
                    if pof>cof:
                        ob.discountprice = int(ob.price-(ob.price*(pof/100)))
                        ob.save()
                    else:
                        ob.discountprice = int(ob.price-(ob.price*(cof/100)))
                        ob.save()
            except:
                try:
                    if coffer:
                        ob.discountprice = int(ob.price-(ob.price*(cof/100)))
                        ob.save()
                except:
                    ob.discountprice = ob.price
                    ob.save()  
    count = ob1.count()
    page = request.GET.get('page', 1)
    paginator = Paginator(ob1, 10)
    try:
        prod = paginator.page(page)
    except PageNotAnInteger:
        prod = paginator.page(1)
    except:
        prod = paginator.page(paginator.num_pages)
    return render(request,'products.html',{'cntx': prod,'inst':inst2,'count':count})