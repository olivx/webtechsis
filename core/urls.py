from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'produtos/$', views.produtos, name='product_list'),
    url(r'produtos/save/$', views.produtos_save, name='save_produtos'),
]
