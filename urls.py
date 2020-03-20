from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('login/', include('django.contrib.auth.urls')), 
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]