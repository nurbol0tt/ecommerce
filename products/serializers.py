from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

# from .documents import NewsDocument
from .models import Product, Category, Media, Brand, ProductAttributeValue, ProductInventory


# class NewsDocumentsSerializers(DocumentSerializer):
#     class Meta:
#         model = Product
#         document = NewsDocument
#
#         fields = ('name', 'description')
#
#         def get_location(self, obj):
#             try:
#                 return obj.location.to_dict()
#             except:
#                 return {}
#

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'is_active')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name',)
