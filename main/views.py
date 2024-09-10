from django.shortcuts import render
from .models import Product

def main(request):
    context = {
        'name': 'Shaney Zoya Fiandi',
        'npm': '2306215923',
        'app_name': 'Yarnsie',
        'class': 'PBP C',
    }
    return render(request, 'main.html', context)

def products(request):
    product_list = Product.objects.all()
    context = {
        'products': product_list,
    }
    return render(request, 'products.html', context)