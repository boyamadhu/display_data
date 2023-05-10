"""prime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app1.views import  *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register,name='register'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('prime/',prime,name='prime'),
    path('create_account/',create_account,name='create_account'),
    path('dummy/',dummy,name='dummy'),
    path('prime_home/',prime_home,name='prime_home'),
    path('catagories/',catagories,name='catagories'),
    path('store/',store,name='store'),
    path('display_profile/',display_profile,name='display_profile'),
    path('practice/',practice,name='practice'),
    path('update_password/',update_password,name='update_password'),
    path('forgot_password/',forgot_password,name='forgot_password'),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
