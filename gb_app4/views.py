from django.shortcuts import render, redirect
from .models import Product
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm


def index(request):
    return render(request, 'gb_app4/index.html')


def all_products(request):
    prods = Product.objects.all()
    return render(request, 'gb_app4/all_products.html', {'prods': prods})


def add_prod_picture(request, prod_id):
    prod = Product.objects.filter(pk=prod_id).first()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            file_url = fs.url(filename)
            prod.image_us = file_url
            prod.save(update_fields=['image_us'])
    else:
        form = ImageForm()
    return render(request, 'gb_app4/add_prod_picture.html', {'pr': prod, 'form': form})

