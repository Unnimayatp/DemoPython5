from .import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('demo',views.demo,name='demo'),

   ]