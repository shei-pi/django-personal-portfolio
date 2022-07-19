from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Project


def home(request):
    projects = Project.objects.all()
    
    return render(request, 'portfolio/home.html', context={'user':'Shei','projects': projects})

class Pong(View):
    
     """ Respond to ping requests"""
     
     def get(self, request):
         """Handle get Request"""
         return HttpResponse("pong")