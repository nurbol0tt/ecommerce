from django.urls import path

from products.views import views_category

urlpatterns = [
    # path('search/', views.PublisherDocumentsView.as_view({'get': 'list'})),
    path('categories/', views_category.CategoryListView.as_view()),
    path('category_add/', views_category.CategoryCreateView.as_view()),
    path('category/<int:pk>/detail/', views_category.CategoryDetailView.as_view()),
    path('category/<int:pk>/update/', views_category.CategoryUpdateView.as_view()),
    path('category/<int:pk>/delete/', views_category.CategoryDeleteView.as_view()),
]
