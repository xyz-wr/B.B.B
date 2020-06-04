from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_records, name = 'category_records'),
]