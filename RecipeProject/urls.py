"""
URL configuration for RecipeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from vege.views import *

urlpatterns = [
    path('', home, name='home'),
    path('recipe/', recipe, name='recipe'),
    path('recipe_delete/<id>/', recipe_delete, name='recipe_delete'),
    path('recipe_update/<id>/', recipe_update, name='recipe_update'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
]
