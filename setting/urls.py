from . import views
from django.urls import path

urlpatterns = [
    path('updateVendor/<int:pk>', views.VendorUpdate.as_view()),
    path('updateshoplocation/<int:pk>', views.shop_location_Update.as_view()),
    path('change_password/<int:pk>', views.ChangePasswordView.as_view()),
    ]