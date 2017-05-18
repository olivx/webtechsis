from django.conf.urls import url
from suporte import views

urlpatterns = [
    url(r'licenses/$', views.license_list, name='licenses'),
    url(r'licenses/save/$', views.license_save, name='license_save'),
    url(r'licenses/update/(?P<pk>\d+)/$', views.license_update, name='license_update'),
    url(r'licenses/delete/(?P<pk>\d+)/$', views.license_delete, name='license_delete'),
    url(r'licenses/stop_send_warning/$', views.licese_stop_send_warning, name='stop_send_warning'),
]
