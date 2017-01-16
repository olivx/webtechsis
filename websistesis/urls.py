from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # core urls
    url(r'^$', TemplateView.as_view(template_name='public.html'), name='public'),
    url(r'^index/$', TemplateView.as_view(template_name='index.html'), name='home'),

    # url(r'^licenses/$', core_views.license_prennity, name='licenses'),
    url(r'^licenses/api/$', core_views.license_prennity, name='licenses'),
    url(r'^licenses/api/detail/$', core_views.license_detail, name='licenses_details'),
    url(r'^licenses/api/create/$', core_views.save_lisence_perennity, name='new_lisence'),
    url(r'^licenses/deactive/$', core_views.deactivate_license_perennity, name='deactivate_lisence'),
    url(r'^licenses/autocomplete/$', core_views.autocomplete_clientes),




    # auth urls
    url(r'^login/$', auth_views.login ,{'template_name': u'login.html'}, name='login'),
    url(r'^logout/$' , auth_views.logout , {'next_page' : '/' }, name='logout'),



]
