from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import ProductSerializer
from .models import Product


# Create your views here.
class ProductListViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)