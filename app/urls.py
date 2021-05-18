
from django.urls import path, include
from .views import login_user
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [


    path('accounts/', include('django.contrib.auth.urls')),
    
    path('social-auth/', include('social_django.urls', namespace = 'social')),

    path('',views.home, name='home'),


] 