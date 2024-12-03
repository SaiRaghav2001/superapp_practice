from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resources import PaymentModesResource, UserOwnedModesResource

@admin.register(PaymentMode)
class PaymentModeAdmin(admin.ModelAdmin):
    list_display = ['payment_mode_name', 'status']


@admin.register(PaymentModes)
class PaymentModesAdmin(ImportExportModelAdmin):
    resource_class = PaymentModesResource
    list_display = ('paymentMode', 'aggregatorName', 'status')
    search_fields = ('paymentMode', 'aggregatorName', 'status')


@admin.register(UserOwnedModes)
class UserOwnedModesAdmin(ImportExportModelAdmin):
    resource_class = UserOwnedModesResource
    list_display = ('user', 'mode', 'status', 'created_at', 'last_used')
    search_fields = ('user__email', 'mode__paymentMode', 'status')

@admin.register(PayuBanksInfo)
class PayuBanksInfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["bankName", "bankCode"]

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ["channel", "price", "status"]