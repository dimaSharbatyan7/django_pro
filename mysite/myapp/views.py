from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    items = Product.objects.all()
    context = {
        "items": items
    }
    return render(request, "myapp/index.html", context)

def index_items(request,my_id):
    item = Product.objects.get(id=my_id)
    context = {
        "item": item
    }
    return render(request, 'myapp/detail.html', context)

