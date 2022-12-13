from django.urls import path, include


urlpatterns = [
    path('location/', include('location.urls')),
    path('product/', include('product.urls')),
    path('news/', include('News.urls')),
    path('Cart/', include('Cart.url')),
    path('profile/', include('Profile.urls')),
    path('setting/', include('setting.urls')),
    path('order/', include('order.urls')),
    path('notification/', include('notification.urls')),
    path('sreach/', include('search.urls')),
    path('adverts/', include('adverts.urls'))

]