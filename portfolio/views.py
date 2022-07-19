from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from .models import Project


def home(request):
    projects = Project.objects.all()
    
    return render(request, 'portfolio/home.html', context={'user':'Shei','projects': projects})

@require_http_methods(["GET", "HEAD", "OPTIONS"])     
def pong(request):
    """Repond to ping"""
    if request.method in ["GET", "HEAD"]:
        return HttpResponse("pong")
    else:
        response = HttpResponse()
        response['Allow'] = ", ".join(["GET", "HEAD", "OPTIONS"])
        return response
    
class Status(TemplateView):
    
    template_name = "portfolio/status.html"
    extra_context = {"status":"Good"}