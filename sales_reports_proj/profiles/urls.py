from django.urls import path
from .views import user_profile_view

app_name = 'profiles'

urlpatterns = [
    path('', user_profile_view, name='profile_view')
]
