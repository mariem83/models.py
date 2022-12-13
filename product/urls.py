from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.CreateProduct.as_view()),
    path('get/', views.GetProductList.as_view()),
    path('get/<int:pk>', views.GetProductDetail.as_view()),
    path('Category/get', views.GetCategoryList.as_view()),
]