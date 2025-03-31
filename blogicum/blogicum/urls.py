<<<<<<< HEAD
=======
"""blogicum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# blogicum/urls.py

>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
<<<<<<< HEAD
    path('auth/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pages.views.handler404'
handler403 = 'pages.views.csrf_failure_view'
handler500 = 'pages.views.handler500'
=======
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430
