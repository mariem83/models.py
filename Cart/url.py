from . import views
from django.urls import path

urlpatterns = [
    path('CreatCart', views.CreateCart.as_view()),
    path('GetCart/<int:UserId>', views.GetCart.as_view()),
    path('DelCart/<int:pk>', views.DeleteCart.as_view()),

]