from django.contrib import admin
from django.urls import path
import search.views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', search.views.SearchFormView),
    path('', search.views.search),
    path('search', search.views.search)
]
