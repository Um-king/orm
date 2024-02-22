from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('<int:pk>/', views.productdetail, name='productdetail'),
]
