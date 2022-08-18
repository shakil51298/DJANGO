from http.client import HTTPResponse
from pickle import TRUE
from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.

def index(request):
    pr1  = Products()
    pr1.id = 1
    pr1.img = 'shoes1.png'
    pr1.name = 'shoes'
    pr1.price = 100
    pr1.desc = "lorem       sdjksl;l;k  "
    pr1.off = False

    pr2  = Products()
    pr2.id = 2
    pr2.img = 'shoes5.png'
    pr2.name = 'something'
    pr2.price = 120
    pr2.desc = "this is desc "
    pr2.off = True

    pr3  = Products()
    pr3.id = 3
    pr3.img = 't_shart.png'
    pr3.name = 'shakil'
    pr3.price = 400
    pr3.desc = "this is desc no 3  "
    pr3.off = False

    products = [pr1, pr2, pr3]
    return render(request, 'index.html', {'products' : products}) 