"""sisgraf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
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

    url(r'^lisences/$', core_views.license_prennity, name='licenses'),
    url(r'^lisences/details/(\d+)/$', core_views.license_detail, name='licenses_details'),
    url(r'^lisences/create/$', core_views.save_lisence_perennity, name='new_lisence'),
    url(r'^lisences/autocomplete/$', core_views.autocomplete_clientes),




    # auth urls
    url(r'^login/$', auth_views.login ,{'template_name': u'login.html'}, name='login'),
    url(r'^logout/$' , auth_views.logout , {'next_page' : '/' }, name='logout'),



]
