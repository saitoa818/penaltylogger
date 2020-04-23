from django.urls import path
from . import views
from .views import LogList


urlpatterns = [
    path('', views.LogList.as_view(), name='log_list'),
    path('log/<int:pk>/', views.log_detail, name='log_detail'),
    path('log/new/', views.log_new, name='log_new'),
    #path('log/<int:pk>/edit/', views.log_edit, name='log_edit'),
    #path('log/confirm/', views.log_confirm, name='log_confirm'),
    path('log/save/', views.log_save, name='log_save'),
    path('login/', views.login, name='login'),
    # path('^$', views.LogList.as_view(), name='index'),
    # path('^add/$', views.MesAddView.as_view(), name='add'),
    # path('^change/(?P<pk>[0-9]+)/$', views.MesChangeView.as_view(), name='change'),
    # path('', views.MesDeleteView.as_view(), name='delete'),
]