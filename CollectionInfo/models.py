from django.db import models
from CustomUser.models import *

# Create your models here.

class PaymentRequest(models.Model):
    SUCCESS = 'Success'
    PENDING = 'Pending'
    EXPIRED = 'Expired'
    DECLINED = 'Declined'
    FAILED = 'Failed'

    STATUS_CHOICES = [
        (SUCCESS, 'Success'),
        (PENDING, 'Pending'),
        (EXPIRED, 'Expired'),
        (DECLINED, 'Declined'),
        (FAILED, 'Failed')
    ]

    internal_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile_crm', null=True, blank=True)
    register_no_or_cust_id = models.CharField(
        max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=PENDING)

    payment_gateway = models.CharField(max_length=250, null=True, blank=True)
    gateway_order_id = models.CharField(max_length=250, null=True, blank=True)
    gateway_charges = models.DecimalField( max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    gateway_session_id = models.CharField(
        max_length=250, null=True, blank=True)
    gateway_message = models.CharField(max_length=300, blank=True, null=True)
    payment_type = models.CharField(max_length=300, blank=True, null=True)
    payment_parm = models.CharField(max_length=300, blank=True, null=True)
    indent_vpa_uri = models.JSONField(null=True, blank=True)
    
    channel = models.CharField(max_length=255, null=True, blank=True)
    item = models.CharField(max_length=255, null=True, blank=True)

    loyalti_transaction_type = models.CharField(
        max_length=250, blank=True, null=True)
    gross_amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    special_coupon = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    e_point = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    i_point = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    cgst_sgst = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    net_paid = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, default=0)

    amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    crmId = models.CharField(max_length=255, null=True, blank=True)
    transaction_number = models.CharField(
        max_length=255, null=True, blank=True)
    billNumberOrInvoiceNumber = models.CharField(
        max_length=255, null=True, blank=True)
    transactionReferenceNumber = models.CharField(
        max_length=255, null=True, blank=True)

    requested_employee_id = models.CharField(
        max_length=255, null=True, blank=True)
    requested_employee_name = models.CharField(
        max_length=255, null=True, blank=True)
    requested_employee_mobile = models.CharField(
        max_length=255, null=True, blank=True)
    requested_employee_location = models.CharField(
        max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    channel = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    dont_show = models.BooleanField(default=False)
    callBackUrl = models.URLField(max_length=500,blank=True, null=True)
    payu_webhook_call = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'PAYMENT REQUEST'
        verbose_name_plural = 'PAYMENT REQUEST'

    def __str__(self) -> str:
        return self.name


class PaymentTransaction(models.Model):
    SUCCESS = 'Success'
    PENDING = 'Pending'
    EXPIRED = 'Expired'
    FAILED = 'Failed'
    ERROR = 'Error'

    STATUS_CHOICES = [
        (SUCCESS, 'Success'),
        (PENDING, 'Pending'),
        (EXPIRED, 'Expired'),
        (FAILED, 'Failed'),
        (ERROR, 'Error'),
    ]

    crm_profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='crm_profile', null=True, blank=True)
    payment_instance = models.ForeignKey(
        PaymentRequest, on_delete=models.PROTECT, related_name='payment_transaction', null=True, blank=True)
    booking_instance = models.ForeignKey(
        'BookingInfo.AppBooking', on_delete=models.PROTECT, related_name='booking_transaction', null=True, blank=True)
    transaction_reference_no = models.CharField(
        max_length=255, null=True, blank=True)
    transaction_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=PENDING)
    mode_of_payment = models.CharField(max_length=255, null=True, blank=True)
    transaction_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    transaction_charge = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    gross_amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    total_transaction_amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'PAYMENT TRANSACTION'
        verbose_name_plural = 'PAYMENT TRANSACTION'


class PaymentSource(models.Model):
    order_id = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True) 
    phoneNumber = models.CharField(max_length=255, null=True, blank=True) 
    source = models.CharField(max_length=255, null=True, blank=True)
    merchant_type = models.CharField(max_length=255, null=True, blank=True)
    payment_details = models.JSONField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 

    class Meta:
        verbose_name = 'PAYMENT SOURCE'
        verbose_name_plural = 'PAYMENT SOURCE'