from django.contrib import admin

# Register your models here.
from suporte.forms import LicenseForm
from suporte.models import PerennityLicense


@admin.register(PerennityLicense)
class PerennityLicenseAdmin(admin.ModelAdmin):
    form = LicenseForm
