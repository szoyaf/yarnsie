from django.shortcuts import render,redirect
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    product = Product.objects.all()

    context = {
        'name': 'Shaney Zoya Fiandi',
        'npm': '2306215923',
        'app_name': 'Yarnsie',
        'class': 'PBP C',
        'product': product,
    }
    return render(request, 'main.html', context)

def products(request):
    product_list = Product.objects.all()
    context = {
        'products': product_list,
    }
    return render(request, 'products.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

