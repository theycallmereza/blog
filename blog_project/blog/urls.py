from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
]