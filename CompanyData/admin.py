from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(City)
class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title']


@admin.register(Outlet)
class OutletAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['city', 'channel', 'status', 'sap_outlet_name', 'name']


@admin.register(TermsConditions)
class TermsConditionsAdmin(admin.ModelAdmin):
    list_display = ["charges_term", "charges_more_term"]

@admin.register(AppVersion)
class AppVersionAdmin(admin.ModelAdmin):
    list_display = ['version_name', 'version_description', 'version_number',
                    'version_notes', 'version_remarks', 'version_status']