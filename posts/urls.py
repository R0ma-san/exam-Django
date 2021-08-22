from django.urls import path
from django.urls.resolvers import URLPattern
from .views import post, post_detail, new_post, post_edit, post_delete, my_posts

urlpatterns = [
    path('', post, name='posts'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('new/', new_post, name='new_post'),
    path('<int:pk>/edit/', post_edit, name='post_edit'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),
    path('my_posts',my_posts ,name='my_posts')
]