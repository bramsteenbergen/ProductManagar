from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import product
from .forms import addProductForm
from django.shortcuts import render

import sys

from django.views.generic.list import ListView

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the products index.")

def test_add_user_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addProductForm(request.POST)
        form.id = -1
        # check whether it's valid:
        if form.is_valid():
            p = product(name=request.POST["name"],
                        alp_num_code=request.POST["alp_num_code"],
                        stock=request.POST["stock"],
                        description=request.POST["description"])
            if p is not None:
                p.save()
                return HttpResponse("Saving succesfull")
            else:
                return HttpResponse("Post attributes have wrong format")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = addProductForm()
        form.id = -1
    return render(request, 'addProduct.html', {'form': form})

def listProducts(request):
    product_list = product.objects.all()

    return render(request, 'product_list.html', {'object_list': product_list})

def viewProduct(request, ID):
    product_obj = product.objects.get(pk=ID)

    return render(request, 'product.html', {'object': product_obj})

def updateProduct(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            product.objects.filter(pk = request.POST["id"]).update(name=request.POST["name"],
                                                                   alp_num_code=request.POST["alp_num_code"],
                                                                   stock=request.POST["stock"],
                                                                   description=request.POST["description"])

            return HttpResponse("Update succesfull")
        else:
            return HttpResponse("Form not Valid")
    # if a GET (or any other method) we'll create a blank form
    else:
        object = product.objects.filter(pk = request.GET["id"])

        print(sys.stderr, object)

        name = object[0].name
        alp_num_code = object[0].alp_num_code
        stock = object[0].stock
        description = object[0].description

        form = addProductForm(initial={'id': request.GET["id"],
                                       'name': name,
                                       'alp_num_code': alp_num_code,
                                       'stock': stock,
                                       'description': description})

    return render(request, 'updateProduct.html', {'form': form})

def deleteProduct(request):
    product.objects.filter(pk=request.GET["id"]).delete()
    return HttpResponse("Delete succesfull")