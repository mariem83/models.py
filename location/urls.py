from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.CreateLocation.as_view()),
    path('get/', views.GetLocationList.as_view()),
    path('get/<int:pk>', views.GetLocation.as_view()),
    path('del/<int:pk>', views.DelLocation.as_view()),
    path('put/<int:pk>', views.UpdateLocation.as_view()),
    path('PrimaryLocation/<int:UserId>', views.GetPrimaryLocation1.as_view()),

    # path('Auth', views.AllUser.as_view()),
]