from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('', views.index, name='home'),
    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path('post_edit/<slug:slug>', views.PostEdit.as_view(), name='post_edit'),
    path(
        'post_delete/<slug:slug>',
        views.PostDelete.as_view(), name='post_delete'),   
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]