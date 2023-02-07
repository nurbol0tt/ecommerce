# from django_elasticsearch_dsl import Document, fields, Index
# from django_elasticsearch_dsl.registries import registry
#
# from .models import Product
#
# PUBLISHER_INDEX = Index('elastic_demo')
#
# PUBLISHER_INDEX.settings(
#     number_of_shards=1,
#     number_of_replicas=1
# )
#
#
# @PUBLISHER_INDEX.doc_type
# class NewsDocument(Document):
#     id = fields.IntegerField(attr="id")
#     title = fields.TextField(
#         fields={
#             "raw": {
#                 "type": 'keyword'
#             }
#         }
#     )
#
#     content = fields.TextField(
#         fields={
#             "raw": {
#                 "type": 'keyword'
#             }
#         }
#     )
#
#     class Django:
#         model = Product
#
#
# @registry.register_document
# class ProductDocument(Document):
#
#     class Index:
#         name = "product"
#
#     class Django:
#         model = Product
#         fields = ("id", "name", "description")
