from django.urls import path
from . import views


urlpatterns = [
    path('', views.picture_of_a_day, name='picture_of_a_day'),
]
