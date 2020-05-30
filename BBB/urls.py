from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.views.login),
    path('records/', include('bookbank.urls')),
    path('account/', include('account.urls')),
]
=======
from django.urls import path
import search.views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', search.views.SearchFormView),
    path('', search.views.search),
    path('search', search.views.search)
]
>>>>>>> b403515148526bc063893136857eacd6c6dedd1d
