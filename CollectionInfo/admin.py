from django.contrib import admin

# Register your models here.
from . import models
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin, ExportActionMixin, ImportMixin


@admin.register(models.PaymentRequest)
class PaymentRequestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['internal_profile', 'phone',
                    'name', 'amount', 'created_at', 'modified_at']
    search_fields = ['internal_profile__phone','phone','name','gateway_order_id','crmId','payment_gateway']


@admin.register(models.PaymentTransaction)
class PaymentTransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['transaction_reference_no', 'transaction_status', 'mode_of_payment',
                    'transaction_date', 'transaction_charge', 'total_transaction_amount', 'remarks']
    search_fields = ['transaction_reference_no',
                     'transaction_status', 'mode_of_payment', 'transaction_date']
    

@admin.register(models.PaymentSource)
class PaymentSourceAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'amount',
                    'phoneNumber', 'source', 'created_at']
    search_fields = ['order_id', 'amount',
                    'phoneNumber', 'source', 'created_at']
