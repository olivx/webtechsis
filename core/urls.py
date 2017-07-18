from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'produtos/$', views.produtos, name='product_list'),
    url(r'produtos/save/$', views.produto_save, name='save_produto'),
    url(r'produtos/update/(?P<pk>\d+)/$', views.produto_update, name='update_produto'),
    url(r'produtos/delete/(?P<pk>\d+)/$', views.produto_delete, name='delete_produto'),

    url(r'clientes/$',views.contrato_client_list, name='contato_cliente_list'),
]
