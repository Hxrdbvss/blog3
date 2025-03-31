from django.shortcuts import render
from django.views.generic import TemplateView
def index(request):
    context = {"posts": posts}
    return render(request, "blog/index.html", context)

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class RulesPageView(TemplateView):
    template_name = 'pages/rules.html'
