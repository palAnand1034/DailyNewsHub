from django.conf.urls import url
from . import views

urlpatterns = [
    # For Admin Panel Category List
    url(r'^panel/category/list/$', views.cat_list, name='cat_list'),
    
    # For Admin Panel Category Add
    url(r'^panel/category/add/$', views.cat_add, name='cat_add'),    
    
    # To download/export CSV file
    url(r'^export/cat/csv/$', views.export_cat_csv, name='export_cat_csv'),   
    
    # To import CSV file
    url(r'^import/cat/csv/$', views.import_cat_csv, name='import_cat_csv'),  
    
    # Existing URLs for editing and deleting categories
    url(r'^panel/category/edit/(?P<cat_id>\d+)/$', views.cat_edit, name='cat_edit'),  # Edit Category
    url(r'^panel/category/delete/(?P<cat_id>\d+)/$', views.cat_delete, name='cat_delete'),  # Delete Category
]
