from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^panel/subcategory/list/$', views.subcat_list, name='subcat_list'),
    url(r'^panel/subcategory/add/$', views.subcat_add, name='subcat_add'),
    url(r'^panel/subcategory/edit/(?P<pk>\d+)/$', views.subcat_edit, name='subcat_edit'),  # Edit URL
    url(r'^panel/subcategory/delete/(?P<pk>\d+)/$', views.subcat_delete, name='subcat_delete'),  # Delete URL
]
