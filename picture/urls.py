from django.urls import path, register_converter
from datetime import datetime
from . import views

urlpatterns = [
    path('', views.all_pictures, name='all_pictures'),
    path('<int:id>/', views.picture_day, name='picture_day'),
]
