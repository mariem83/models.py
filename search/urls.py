from django.urls import path
from . import views

urlpatterns = [
    path('pname/', views.SearchProductName.as_view()),
    path('pcategory/', views.SearchProductCategory.as_view()),
    path('pshopname/', views.SearchProductShopName.as_view()),
]
