from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Brand, Category
from products.serializers import BrandSerializer


class BrandListView(APIView):
    """
    Return list of all brands
    """

    def get(self, request):
        brand = Brand.objects.all()
        serializers = BrandSerializer(brand, many=True)
        return Response(serializers.data)


class BrandCreateView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetailView(APIView):

    def get(self, request, pk):
        brand = get_object_or_404(Brand, id=pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)


class BrandUpdateView(APIView):

    def put(self, request, pk):
        brand = get_object_or_404(Brand, id=pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        brand = get_object_or_404(Brand, id=pk)
        brand.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
