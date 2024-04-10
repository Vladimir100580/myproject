from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name=''),       # можно сделать path('main', views.index, name='main')
    path('about/', views.about, name='about'),
]
