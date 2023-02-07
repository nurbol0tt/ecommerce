from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Category, Product
from products.serializers import CategorySerializer


class CategoryListView(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryCreateView(APIView):
    """

    """
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        # products = Product.objects.filter(category=category)

        serializer = CategorySerializer(category)

        if not category:
            return Response({'error': "category does not exist"})
        else:
            return Response({
                "category": serializer.data,
            }
            )


class CategoryUpdateView(APIView):
    """
    Only admin can update Category
    """

    permission_classes = [IsAdminUser]

    def put(self, request, pk, format=None):
        snippet = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteView(APIView):
    """
    Only admin can delete Category
    """
    permission_classes = [IsAdminUser]

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Category, id=pk)
        snippet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
