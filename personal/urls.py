from django.urls import path
import personal.views

urlpatterns = [
    path('', personal.views.user_page, name = "user"),
]