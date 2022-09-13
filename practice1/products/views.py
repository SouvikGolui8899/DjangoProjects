from django.shortcuts import render, get_object_or_404

from .models import Product

from .forms import ProductForm

# Create your views here.

def products_home_view(request):
    object_list = Product.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, 'products/index.html', context)


def products_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/create.html', context)


def products_get_by_id_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, 'products/index.html', context)