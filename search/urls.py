from django.urls import path

from . import views

urlpatterns = [
    path("search/<str:query>/", views.SearchProductInventoryView.as_view()),

]
