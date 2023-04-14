from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('hello world', views.hello_world, name='hello_world'),
    path('image/', views.image_view, name='image-view'),
    
 

]