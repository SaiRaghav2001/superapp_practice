from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import *
from ProfileActivity.models import *
from CustomUser.models import Profile
# Register your models here.


class ProfileAddressInline(admin.TabularInline):
    model = ProfileAddress


class ProfileFbtokenInline(admin.TabularInline):
    model = ProfileFbtoken


class ProfileNoticationPreferenceInline(admin.TabularInline):
    model = ProfileNoticationPreference


class ProfileAoiInline(admin.TabularInline):
    model = ProfileAoi

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['phone', 'gender', 'user']
    inlines = [ProfileAddressInline, ProfileFbtokenInline,
               ProfileNoticationPreferenceInline, ProfileAoiInline]
    search_fields = ['phone', 'pan_number']


@admin.register(ProfileVerification)
class ProfileVerificationAdmin(admin.ModelAdmin):
    list_display = ['profile', 'pan_number',
                    'name_as_per_pan', 'dob', 'pan_image', 'verified_pan']
    search_fields = ['profile__phone', 'pan_number', 'name_as_per_pan', 'dob']