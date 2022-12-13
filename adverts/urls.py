from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UploadAds.as_view()),
    path('get/<int:pk>', views.RetrieveAds.as_view()),
]
