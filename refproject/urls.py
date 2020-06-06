"""refproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

admin.site.site_header = "Medeaz| HRM"
admin.site.site_title = "Medeaz"
admin.site.index_title = "HRM"

from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, urlpatterns
from reapp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('admin/', admin.site.urls),
    path('med-hrms/',include('reapp.urls')),
    path('login/',views.login,name='login'),
	path('logout',views.logout,name='logout'),
	path('forgot_password', views.forgot_password, name='forgot_password'),
    path('otp', views.otp, name='otp'),
    path('reset_password', views.reset_password, name='reset_password'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
