from django.urls import path
import search.views

urlpatterns = [
    path('', search.views.search, name = "search"),
]
