"""dj_personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from portfolio.views import home
from portfolio.views import Status, pong
urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('ping/', pong, name='ping'),
    path('status/', Status.as_view(), name='site_status')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)