from django.shortcuts import render
from . models import men,men_detail,women,women_detail,ad

def home(request):
    return render(request,"index.html")

def ads(request, *args, **kwargs):
    a= ad.objects.get(pk=id) 
    context = {'ad' : a}
    return render(request, "index.html", context)