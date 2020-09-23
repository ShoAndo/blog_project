from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.TopView.as_view(), name="index"),
  path('home/', views.HomeView.as_view(), name="home"),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.SignUpView.as_view(), name="signup"),
  path('list/', views.TweetList.as_view(),name="list"),
  path('edit/<int:pk>', views.TweetEdit.as_view(), name="edit"),
  path('new/', views.NewTweet.as_view(), name="new"),
  path('delete/<int:pk>', views.DeleteTweet.as_view(), name="delete"),
]