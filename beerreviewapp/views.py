from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'beerreviewapp/index.html')

def beertypes (request):
    type_list=ProductType.objects.all()
    return render(request, 'beerreviewapp/types.html', {'type_list': type_list})

def getproducts(request):
    product_list=Product.objects.all()
    return render (request, 'beerreviewapp/products.html', {'product_list': product_list})

def productdetail(request, id):
    detail=get_object_or_404(Product, pk=id)
    context = { 'detail': detail}
    return render (request, 'beerreviewapp/details.html',context=context )
#form view
@login_required
def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'beerreviewapp/newproduct.html', {'form': form})

def loginmessage(request):
     return render(request, 'beerreviewapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'beerreviewapp/logoutmessage.html')