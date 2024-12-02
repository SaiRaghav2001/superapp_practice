from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin, ExportActionMixin, ImportMixin
from django.contrib.auth.models import User
from import_export import resources


class ProfileAddressInline(admin.TabularInline):
    model = models.ProfileAddress

@admin.register(models.ProfileAddress)
class ProfileAddressAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['profile', 'type_of_address', 'status']

@admin.register(models.ProfileActivity)
class ProfileActivityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['profile', 'type', 'instance']
    search_fields = ['type', 'instance']


@admin.register(models.Enquirylog)
class EnquirylogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['type_of_enq', 'name', 'model', 'mobile',
                    'email', 'item_description', 'enquire_at', 'scheduled',]
    search_fields = ['mobile']

@admin.register(models.ProfileSearch)
class ProfileSearchAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['profile', 'keyword', 'search_at']

@admin.register(models.Wishlist)
class WishlistAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['profile', 'item']
    search_fields = ['item']