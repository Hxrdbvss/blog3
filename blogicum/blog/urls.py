from django.urls import path
from .views import index, post_detail, edit_profile, add_comment, create_post, category_posts, register, profile, edit_profile

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('category/<str:category_slug>/', category_posts, name='category_posts'),
    path('auth/registration/', register, name='register'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:post_id>/comment/', add_comment, name='add_comment'),  
    path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
]   