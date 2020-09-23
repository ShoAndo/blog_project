from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.TopView.as_view(), name="index"),
  path('home/', views.HomeView.as_view(), name="home"),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.SignUpView.as_view(), name="signup"),
  #path('list/', views.TweetList.as_view(),name="list")
]