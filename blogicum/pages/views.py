from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class RulesPageView(TemplateView):
    template_name = 'pages/rules.html'

# Обработчик для 404
def handler404(request, exception):
    return render(request, 'pages/404.html', status=404)

# Обработчик для 403 CSRF
def csrf_failure_view(request, reason=""):
    return render(request, 'pages/403csrf.html', {'reason': reason}, status=403)

# Обработчик для 500
def handler500(request):
    return render(request, 'pages/500.html', status=500)
=======

def index(request):
    context = {"posts": posts}
    return render(request, "blog/index.html", context)

def about(request):
    return render(request, 'pages/about.html')

def rules(request):
    return render(request, 'pages/rules.html')
>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430
