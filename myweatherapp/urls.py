from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_404',views.test_404,name='test_404'),
]