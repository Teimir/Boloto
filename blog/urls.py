"""
URL configuration for boloto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings



urlpatterns = [
    path('', views.boloto, name='boloto'),
    path('contacts/', views.contacts, name='blog-cont'),
    path('create/', views.create, name='create'),
    path("login/", views.loginView, name='login'),
    path("signup/", views.SignupView, name='signup'),
#    path('posts/create/', create_post_view, name='create_post'),
#    path('posts/<int:pk>/', post_detail_view, name='post_detail'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('profile/<username>/', views.profile_view, name='profile')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
