from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render

# Обработчик для 403 CSRF
def csrf_failure_view(request, reason=""):
    return render(request, 'pages/403_csrf.html', {'reason': reason}, status=403)

# Обработчики для 404 и 500
def handler404(request, exception):
    return render(request, 'pages/404.html', status=404)

def handler500(request):
    return render(request, 'pages/500.html', status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('auth/', include('django.contrib.auth.urls')),  # Маршруты авторизации
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)