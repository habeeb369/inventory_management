from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse


from .models import products
from .forms import proform


# Create your views here.

def index(request):
    return render(request,'home.html')
def add(request):
    return render(request,'add.html')

def saveUser(request):
    if request.method=="POST":
        sr=products()
        sr.product_id=request.POST.get('id')
        sr.name=request.POST.get('name')
        sr.price=request.POST.get('price')
        sr.quantity=request.POST.get('quantity')
        sr.save()

    return render(request,'add.html')
def list(request):
    productdata=products.objects.all()
    mydict={
        'data':productdata
    }
    return render(request,'list.html',context=mydict)

def list2(request):
    productdata=products.objects.all()
    mydict={
        'data':productdata
    }
    return render(request,'list2.html',context=mydict)

def delete(request,pk):
    obj = get_object_or_404(products,pk=pk)
    obj.delete()
    return render(request,'deleted.html')

def edit(request,product_id):
    product = get_object_or_404(products, id=product_id)
    if request.method == 'POST':
        form = proform(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request,'saved.html')  # Redirect to product list page
    else:
        form = proform(instance=product)
    return render(request, 'edit_product.html', {'form': form})







