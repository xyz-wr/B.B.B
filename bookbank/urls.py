from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name = "record_list"),
    path('<int:record_id>', views.detail, name = "record_detail"),
    path('new', views.new, name = "record_new"),
    path('edit/<int:record_id>', views.edit, name = 'record_edit') ,
    path('update/<int:record_id>', views.update, name = 'record_update'),
    path('delete/<int:record_id>', views.delete, name = 'record_delete'),
]