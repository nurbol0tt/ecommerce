from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, CompoundSearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

# from .documents import NewsDocument
from products.serializers import NewsDocumentsSerializers


# Create your views here.
# class PublisherDocumentsView(DocumentViewSet):
#     document = NewsDocument
#     serializer_class = NewsDocumentsSerializers
#
#     filter_backends = [
#         FilteringFilterBackend,
#         CompoundSearchFilterBackend
#     ]
#
#     search_fields = ('name', 'description')
#     multi_match_search_fields = ('name', 'description')
#
#     filter_fields = {
#         'name': 'name',
#         'description': 'description'
#     }