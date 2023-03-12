from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
]