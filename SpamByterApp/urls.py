from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Register', views.Register, name='Register'),
]