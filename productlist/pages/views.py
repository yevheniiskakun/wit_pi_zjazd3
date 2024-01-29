from django.shortcuts import render, redirect

from .models import Product, ProductSerializer

from rest_framework import permissions, viewsets, generics
from rest_framework.response import Response

def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/index.html', context)

def add_product(request):
    pass

def delete_product(request, id):
    pass


def mark_product(request, id):
    pass

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


class MarkProduct(generics.UpdateAPIView):
    """
        API endpoint that allows products to be updated.
    """

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

class ProductAdd(generics.ListCreateAPIView):
    """
        API endpoint that allows products to be created.
    """
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = WomenSerializer