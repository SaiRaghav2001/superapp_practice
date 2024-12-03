from django.contrib import admin
from . models import * 
from import_export.admin import ImportExportModelAdmin 

# Register your models here.
@admin.register(Accessory)
class AccessoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['booking_id', 'itemlist','booked_at',  'item_description', 'profile',
                    'address', 'item_price', 'deliverred_time', 'booking_status']
    
@admin.register(AppBooking)
class AppBookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['profile', 'itemlist', 'booked_at',
                    'payment_status', 'payment_id', 'amount', 'crmId']
    search_fields = ['payment_id', 'gateway_order_id', 'crmId','payment_status','source','mode_of_payment','profile__phone']


@admin.register(NewCarBooking)
class NewCarBookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'booked_at', 'profile', 'address', 'item_description',
                    'booking_id', 'city', 'outlets', 'item_price', 'employee_id', 'referred_by', 'booking_status']


@admin.register(UsedCarBooking)
class UsedCarBookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['itemlist', 'item_description','booked_at',  'booking_id', 'profile', 'brand', 'model', 'transmission', 'fuel', 'year', 'phone', 'email',
                    'kms_driven_starting', 'kms_driven_ending', 'price', 'lat', 'long', 'enquire_at', 'scheduled', 'employee_id', 'referred_by','recipient_address','booking_status']


@admin.register(UsedcarSellEnquiry)
class UsedcarSellEnquiryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['address', 'evaluation_type', 'mobile_no', 'booked_at', 'name', 'pincode', 'scheduled_at',
                    'brand', 'vehicle_model', 'vehicle_number', 'vehicle_variant', 'year_of_registration']


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['booking_id', 'itemlist','booked_at',  'item_description', 'profile', 'address', 'name', 'email', 'mobile', 'city', 'outlet',
                    'model', 'varient', 'color', 'pickup_slot', 'item_price', 'employee_id', 'referred_by', 'deliverred_time', 'booking_status']




@admin.register(Insurance)
class InsuranceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['itemlist', 'item_description','booked_at',  'profile', 'address', 'name', 'email', 'mobile', 'registered_number', 'model', 'variant',
                    'fuel', 'reg_date', 'policy_expire_date', 'last_claim_status', 'claim_bonus', 'employee_id', 'referred_by', 'booked_at', 'booking_status']
    

 


