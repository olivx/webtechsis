from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # core urls
    url(r'^contato/$', core_views.contact, name='contato'),

    url(r'^core/cliente/autocomplete/$', core_views.autocomplete_clientes),
    url(r'^core/produto/autocomplete/$', core_views.autocomplete_produtos),

    url(r'^techcd/', include('core.urls', namespace='techcd')),
    url(r'^suporte/', include('suporte.urls', namespace='suporte')),
    url(r'^boletos/', include('faturamento.urls', namespace='boletos')),
    url(r'^contato/enviado/$', TemplateView.as_view(template_name='snippet/obrigado-pelo-contato.html'),
        name='obrigado_pelo_contato'),

    # index login
    url(r'^index/$', TemplateView.as_view(template_name='index.html'), name='home'),

    # index public
    url(r'^$', TemplateView.as_view(template_name='public.html'), name='public'),

    # auth urls
    url(r'^login/$', auth_views.login, {'template_name': u'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

]
