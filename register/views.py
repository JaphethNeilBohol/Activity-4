from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.db.models import Q

def list_register(request):
    query = request.GET.get('q')
    register = Product.objects.all()
    if query:
        register = register.filter(
            Q(product__icontains=query) |
            Q(price__icontains=query) |
            Q(quantity__icontains=query) |
            Q(manufacture_date__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()
    return render(request, 'register/product_list.html', {'register': register})

def add_register(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ProductForm()
    return render(request, 'register/product_form.html', {'form': form})

def edit_register(request, pk):
    register = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=register)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ProductForm(instance=register)
    return render(request, 'register/product_form.html', {'form': form})

def delete_register(request, pk):
    register = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        register.delete()
        return redirect('list')
    return render(request, 'register/product_confirm_delete.html', {'register': register})
# Create your views here.
