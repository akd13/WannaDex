from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getscores', views.getscores, name='getscores'),
    path('getscorescustom',views.getscorescustom, name='getscorescustom')
]