from django.contrib import admin
from django.urls import path,include
import account.views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.views.login),
    path('records/', include('bookbank.urls')),
    path('account/', include('account.urls')),
    path('search/', include('search.urls')),
    path('user/', include('personal.urls')),
    path('category/', include('category.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)