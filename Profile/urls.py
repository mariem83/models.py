from . import views
from django.urls import path

urlpatterns = [
    path('Profile/<int:uid>', views.ProfilePrudect.as_view()),
    path('News/<int:uid>', views.ProfileNews.as_view()),
    path('vendor-comment-and-replay-info/<int:uid>', views.VendorCommentAndReplayInfo.as_view()),
    path('CreateComment', views.CreateComment.as_view()),
    path('CreateReplay', views.CreateReaplay.as_view()),
    path('ProfileVendor/<int:pk>', views.VendorProfile.as_view()),
    path('CustomerProfile/<int:pk>', views.CustomerProfile.as_view()),

]