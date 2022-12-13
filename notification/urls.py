from . import views
from django.urls import path

urlpatterns = [
    path('getlist/<int:pk>', views.ListNotification.as_view()),
    path('create/', views.CreateNotification.as_view()),
    path('getdesc/<int:pk>', views.RetrieveNotification.as_view())
]