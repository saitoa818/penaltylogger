from django.urls import path
from . import views
from .views import LogList



urlpatterns = [
    path('', views.LogList.as_view(), name='log_list'),
    path('log/<int:pk>/', views.log_detail, name='log_detail'),
    path('log/new/', views.log_new, name='log_new'),
    path('log/save/', views.log_save, name='log_save'),
    path('login/',  views.login.as_view(), name='login'),
]