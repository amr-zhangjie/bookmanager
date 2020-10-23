"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publish_list/', views.publish_list),
    # path('publish_add/', views.publish_add),
    path('publish_add/', views.PublisherAdd.as_view()),
    path('publish_del/', views.publish_del),
    path('publish_edit/', views.publish_edit),

    path('book_list/', views.book_list),
    path('book_add/', views.book_add),
    path('book_del/', views.book_del),
    path('book_edit/', views.book_edit),

    path('author_list/', views.author_list),
    path('author_add/', views.author_add),
    path('author_del/', views.author_del),
    path('author_edit/', views.author_edit),





]