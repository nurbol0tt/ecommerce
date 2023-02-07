from django.urls import path

from products.views import views_brand

urlpatterns = [
    path('brands/', views_brand.BrandListView.as_view()),
    path('brand/create/', views_brand.BrandCreateView.as_view()),
    path('brand/<int:pk>/detail/', views_brand.BrandDetailView.as_view()),
    path('brand/<int:pk>/update/', views_brand.BrandUpdateView.as_view()),
    path('brand/<int:pk>/delete/', views_brand.BrandDeleteView.as_view())
]
