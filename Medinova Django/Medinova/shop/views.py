from django.shortcuts import render
from shop.models import Products
# Create your views here.

def view_showproduct(request):
    allp=Products.objects.all()
    d1={'products':allp}
    resp=render(request,'shop/products.html',context=d1)
    return resp

