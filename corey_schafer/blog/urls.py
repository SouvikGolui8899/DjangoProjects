"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home-view'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts-view'),
    path('post/create/', views.PostCreateView.as_view(), name='create-view'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail-view'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update-view'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-view'),
    path('about', views.about, name='about-view')
]
