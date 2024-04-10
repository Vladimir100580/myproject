from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_products', views.all_products, name='all_products'),
    path('add_prod_picture/<int:prod_id>/', views.add_prod_picture, name='add_prod_picture'),
]

if settings.DEBUG:   # Чтобы иметь доступ к изображениям по url
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)