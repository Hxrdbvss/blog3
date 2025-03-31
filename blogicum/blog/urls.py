from django.urls import path
<<<<<<< HEAD
from .views import index, PageDetailView, PageCreateView, PageUpdateView, delete_post, edit_comment, post_detail, edit_post, delete_comment, edit_profile, add_comment, create_post, category_posts, register, profile, edit_profile
=======
from .views import index, post_detail, category_posts
>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430

app_name = 'blog'

urlpatterns = [
<<<<<<< HEAD
    path('', index, name='index'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('category/<str:category_slug>/', category_posts, name='category_posts'),
    path('auth/registration/', register, name='register'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('posts/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
]  
=======
    path('', index, name='index'),  # Главная страница блога
    path('posts/<int:id>/', post_detail, name='post_detail'),  # Страница отдельного поста
    path('category/<str:category_slug>/', category_posts, name='category_posts'),  # Страница категории
]

>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430
