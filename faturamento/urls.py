from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'list/$', views.boleto_list, name='boletos_list'),
    url(r'detail/techcd/boleto/(?P<nnum_bol>[\d]+)/$', views.boleto_tech_detail, name='boleto_tech_detail'),
    url(r'detail/data-store/boleto/(?P<nnum_bol>[\d]+)/$', views.boleto_data_detail, name='boleto_data_detail'),
    url(r'detail/midia-center/boleto/(?P<nnum_bol>[\d]+)/$', views.boleto_midia_detail, name='boleto_midia_detail'),

    url(r'update/boleto/(?P<nnum_bol>[\d]+)/$', views.boleto_update, name='boleto_update'),
]
