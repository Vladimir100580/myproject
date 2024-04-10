from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.users, name='users1'),
    path('les4/', include('gb_app4.urls')),
    path('user/<int:user_id>/<int:days>', views.user_products, name='user_products'),
]
