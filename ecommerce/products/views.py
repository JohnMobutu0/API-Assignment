from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def home(request):
    return render(request, "products/home.html")

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # pass message
            return redirect("products:add_category")
    else:
        form = CategoryForm()
    return render(request,"products/category_form.html",{'form':form})

def category_list(request):
    categories = Category.objects.all()
    return render(request,"products/category_list.html",{'categories':categories})


# a) View to insert (add) products
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES) # request.FILES is required for images
        if form.is_valid():
            form.save()
            return redirect('products:product_list') # Redirect to the display page after saving
    else:
        form = ProductForm()
    
    return render(request, 'products/add_product.html', {'form': form})

# b) View to display all products
def product_list(request):
    products = Product.objects.all() # Retrieve all product records
    return render(request, 'products/product_list.html', {'products': products})