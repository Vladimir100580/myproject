from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('user/<int:user_id>/<int:days>', views.user_products, name='user_products'),
]
