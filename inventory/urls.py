from django.urls import path
from .views import (
    UserCreateView, StockListCreateView, StockDetailView,
    CategoryListCreateView, CategoryDetailView,
    EquipmentListCreateView, EquipmentDetailView,
    LogoutView
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('stocks/', StockListCreateView.as_view(), name='stock-list-create'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('equipment/', EquipmentListCreateView.as_view(), name='equipment-list-create'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('logout/', LogoutView.as_view(), name='logout')
]
