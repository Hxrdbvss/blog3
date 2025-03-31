from django.urls import path
from . import views

<<<<<<< HEAD
app_name = 'pages'

urlpatterns = [
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('rules/', views.RulesPageView.as_view(), name='rules'),
]
=======
app_name = 'pages'  # Указываем namespace для приложения

urlpatterns = [
    path('about/', views.about, name='about'),  # Страница "about"
    path('rules/', views.rules, name='rules'),  # Страница "rules"
]
>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430
