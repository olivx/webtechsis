from django.contrib import admin

from core.form import LicenseForm
from core.models import PerennityLicense, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'assunto', 'categoria', 'data_created')
    list_filter = ('categoria', 'user')


@admin.register(PerennityLicense)
class PerennityLicense(admin.ModelAdmin):
    form = LicenseForm
