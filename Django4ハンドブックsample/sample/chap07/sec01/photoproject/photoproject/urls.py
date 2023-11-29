from django.contrib import admin
from django.urls import path, include # include追加

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # photo.urlsへのURLパターン
    path('', include('photo.urls')),
]
