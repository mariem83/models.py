from . import views
from django.urls import path
urlpatterns = [
    path('CreateOrder', views.CraeteOrder2.as_view()),

    path('Orderinfo/<int:uid>', views.OrderInfo.as_view()),

]