
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gb_app4.urls')),
    path('les3/', include('gb_app3.urls')),
    # path('__debug__/', include("debug_toolbar.urls")),
]

# https://github.com/Vladimir100580/DJango_GB_HW.git
# echo "export SECRET_KEY=564f3d6969cd309184745f4ccb71e05e621ae802e4525d9f8605bce168ccc107" >> .env
# echo "export MYSQL_PASSWORD=LordLove2024!" >> .env
# echo 'set -a; source ~/gb_site/.env; set +a' >> ~/.virtualenvs/virtualenv/bin/postactivate