from django.contrib import admin
from django.urls import path,include
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.views.login),
    path('records/', include('bookbank.urls')),
    path('account/', include('account.urls')),
    path('search/', include('search.urls')),
    path('user/', include('personal.urls')),
]
