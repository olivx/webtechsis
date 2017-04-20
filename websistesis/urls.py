from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # core urls
    url(r'^$', TemplateView.as_view(template_name='public.html'), name='public'),
    url(r'^index/$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^contato/enviado/$', TemplateView.as_view(template_name='snippet/obrigado-pelo-contato.html'), name='obrigado_pelo_contato'),
    url(r'^contato/$', core_views.contact, name='contato'),

    # rotas novas
    url(r'^licenses/autocomplete/$', core_views.autocomplete_clientes),

    url(r'^licenses/$', core_views.license_list, name='licenses'),
    url(r'^licenses/save/$', core_views.license_save, name='license_save'),
    url(r'^licenses/update/(?P<pk>\d+)/$', core_views.license_update, name='license_update'),
    url(r'^licenses/delete/(?P<pk>\d+)/$', core_views.license_delete, name='license_delete'),


    # faturamento
    url(r'^boletos/' , include('faturamento.urls', namespace='boletos')),


    # auth urls
    url(r'^login/$', auth_views.login ,{'template_name': u'login.html'}, name='login'),
    url(r'^logout/$' , auth_views.logout , {'next_page' : '/' }, name='logout'),



]
