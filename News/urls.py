from . import views
from django.urls import path

urlpatterns = [
    path('get/<int:pk>', views.GetNews.as_view()),
    path('Craete', views.CreateNews.as_view()),
    path('GetAllNews', views.GetNews.as_view()),

]