from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path('post_edit/<slug:slug>', views.PostEdit.as_view(), name='post_edit'),  
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]