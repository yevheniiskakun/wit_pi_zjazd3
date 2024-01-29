from django.shortcuts import render, redirect

from .models import Product, ProductSerializer

from rest_framework import permissions, viewsets, generics

def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/index.html', context)

def add_product(request):
    if request.method == 'POST':
        new_product_name = request.POST.get('new_product')

        if "  " not in new_product_name:
            Product.objects.create(name=new_product_name)

    products = Product.objects.all()
    context = {"products": products}
    return redirect('/')

def delete_product(request, id):
    pass


def mark_product(request, id):
    modified_product = Product.objects.get(id=id)
    if modified_product.buyed == False:
        modified_product.buyed = True  # change field
    else:
        modified_product.buyed = False  # change field
    modified_product.save()  # this will update only
    products = Product.objects.all()
    context = {"products": products}
    return redirect('/')


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ProductDelete(generics.DestroyAPIView):
    """
    API endpoint that allows products to be deleted.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer