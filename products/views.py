from django.db.migrations import serializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, User
from products.producer import publish
from products.serializers import ProductSerializer
import random


class ProductViewSet(viewsets.ViewSet):
    # api list function
    def list(self, request): # /api/products for GET Request
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # API create function
    def create(self, request): # /api/products for POST Request
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('Product_created',serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # API delete function
    def retrieve(self, request, pk= None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk= None): # /api/products/<str:id>
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=products, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('Product_updated',serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk= None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        publish('Product_deleted',pk)
        return Response(status=status.HTTP_204_NO_CONTENT, data="Product Key "+pk+" Deleted")

class UserAPIView(APIView):
        def get(self, _):
            users = User.objects.all()
            user = random.choice(users)
            return Response({
                'id': user.id
            })