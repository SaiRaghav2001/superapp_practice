from django.db import models
from ProfileActivity.models import ProfileAddress
from ProductData.models  import *
from CustomUser.models import Profile

# Create your models here.

class AppBooking(models.Model):
    SUCCESS = 'Success'
    PENDING = 'Pending'
    ERROR = 'Error'
    DECLINED = 'Declined'
    FAILED = 'Failed'
    
    BOOKED = 'Booked'
    INVOICED = 'Invoiced'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (SUCCESS, 'Success'),
        (PENDING, 'Pending'),
        (ERROR, 'Error'),
        (DECLINED, 'Declined'),
        (FAILED, 'Failed')
    ]

    BOOKING_STATUS = [
        (BOOKED, 'Booked'),
        (INVOICED, 'Invoiced'),
        (CANCELLED, 'Cancelled'),
        (PENDING, 'Pending')
    ]

    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, blank=True, null=True)
    itemlist = models.ForeignKey(
        Itemlist, on_delete=models.PROTECT, blank=True, null=True)
    item_description = models.ForeignKey(
        ItemDescription, on_delete=models.PROTECT, blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=PENDING)
    booking_status = models.CharField(
        max_length=50, choices=BOOKING_STATUS, default=PENDING)
    payment_id = models.CharField(
        max_length=250, blank=True, null=True)
    
    gatewayError = models.TextField(blank=True, null=True)

    source = models.CharField(
        max_length=250, blank=True, null=True)

    amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

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

    cust_id_or_reg_no = models.CharField(
        max_length=250, blank=True, null=True)

    mode_of_payment = models.CharField(
        max_length=250, blank=True, null=True)
    payment_type = models.CharField(
        max_length=250, blank=True, null=True)
    payment_param = models.CharField(
        max_length=250, blank=True, null=True)
    gateway_session_id = models.CharField(
        max_length=250, blank=True, null=True)
    gateway_order_id = models.CharField(
        max_length=250, blank=True, null=True)
    gateway_charges = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    gateway_message = models.CharField(max_length=255, blank=True, null=True)
    indent_vpa_uri = models.JSONField(null=True, blank=True)
    crmId = models.CharField(
        max_length=500, blank=True, null=True)
    callBackUrl = models.URLField(max_length=500,blank=True, null=True)
    payment_verified_at = models.DateTimeField(blank=True, null=True)
    payu_webhook_call = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'APEX'
        verbose_name_plural = 'APEX'


class NewCarBooking(models.Model):
    PENDING = 'Pending'
    BOOKED = 'Booked'
    RETAIL = 'Retail'
    RETAILCANCEL = 'RetailCancel'
    DELIVERRED = 'Deliverred'
    FAILED = 'Failed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (BOOKED, 'Booked'),
        (RETAIL, 'Retail'),
        (RETAILCANCEL, 'RetailCancel'),
        (DELIVERRED, 'Deliverred'),
        (FAILED, 'Failed')
    ]
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    mobile = models.CharField(max_length=250, blank=True, null=True)
    cust_id_or_reg_no = models.CharField(
        max_length=250, blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, blank=True, null=True)
    address = models.ForeignKey(
        ProfileAddress, on_delete=models.PROTECT, blank=True, null=True)
    item_description = models.ForeignKey(
        ItemDescription, on_delete=models.PROTECT, blank=True, null=True)
    booking_id = models.ForeignKey(
        AppBooking, related_name="bookin_desc_newcar", on_delete=models.PROTECT, blank=True, null=True)
    
    profilePanCard = models.CharField(max_length=250, blank=True, null=True)
    profilePanName = models.CharField(max_length=250, blank=True, null=True)
    profileBookedFor = models.CharField(max_length=250, blank=True, null=True)
    profileRelationship = models.CharField(max_length=250, blank=True, null=True)
    otherPanNumber = models.CharField(max_length=250, blank=True, null=True)
    panPicOthers = models.ImageField(upload_to='store/images', blank=True, null=True)

    city = models.CharField(max_length=250, blank=True, null=True)
    outlets = models.CharField(max_length=250, blank=True, null=True)
    item_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    referred_by = models.CharField(max_length=255, blank=True, null=True)


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

    booking_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=BOOKED)
    payment_verified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'NEW CAR'
        verbose_name_plural = 'NEW CAR'


class UsedCarBooking(models.Model):

    ENQUIRED = 'Enquired'
    CONTACTED = 'Contacted'
    BOOKED = 'Booked'
    DELIVERRED = 'Deliverred'
    CANCELLED = 'Cancelled'
    CAR_NOT_AVAILABLE = 'Car not available'

    STATUS_CHOICES = [
        (ENQUIRED, 'Enquired'),
        (CONTACTED, 'Contacted'),
        (BOOKED, 'Booked'),
        (DELIVERRED, 'Deliverred'),
        (CANCELLED, 'Cancelled'),
        (CAR_NOT_AVAILABLE, 'Car not available')
    ]

    itemlist = models.ForeignKey(
        Itemlist, on_delete=models.PROTECT, blank=True, null=True)
    item_description = models.ForeignKey(
        ItemDescription, on_delete=models.PROTECT, blank=True, null=True)
    booking_id = models.ForeignKey(
        AppBooking, on_delete=models.PROTECT, blank=True, null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, blank=True, null=True)
    address = models.ForeignKey(
        ProfileAddress, on_delete=models.PROTECT, blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    brand = models.CharField(max_length=250, blank=True, null=True)
    model = models.CharField(max_length=250, blank=True, null=True)
    transmission = models.CharField(max_length=250, blank=True, null=True)
    fuel = models.CharField(max_length=250, blank=True, null=True)
    year = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    cust_id_or_reg_no = models.CharField(
        max_length=250, blank=True, null=True)
    kms_driven_starting = models.CharField(
        max_length=250, blank=True, null=True)
    kms_driven_ending = models.CharField(max_length=250, blank=True, null=True)
    price = models.CharField(max_length=250, blank=True, null=True)
    lat = models.CharField(max_length=250, blank=True, null=True)
    long = models.CharField(max_length=250, blank=True, null=True)
    enquire_at = models.DateTimeField(auto_now_add=True)
    scheduled = models.DateTimeField(auto_now=True, blank=True, null=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    referred_by = models.CharField(max_length=255, blank=True, null=True)
    recipient_address= models.CharField(max_length=255,blank=True,null=True)
    number_of_owners = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    booking_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=ENQUIRED)

    class Meta:
        verbose_name = 'USED CAR - BUY'
        verbose_name_plural = 'USED CAR - BUY'


class Service(models.Model):

    PENDING = 'Pending'
    BOOKED = 'Booked'
    CONTACTED = 'Contacted'
    PICKED = 'Picked Up'
    DELIVERRED = 'Deliverred'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (BOOKED, 'Booked'),
        (CONTACTED, 'Contacted'),
        (PICKED, 'Picked Up'),
        (DELIVERRED, 'Deliverred'),
        (CANCELLED, 'Cancelled')
    ]

    booking_id = models.ForeignKey(
        AppBooking, related_name="bookin_desc_service", on_delete=models.PROTECT, blank=True, null=True)
    itemlist = models.ForeignKey(
        Itemlist, on_delete=models.PROTECT, blank=True, null=True)
    item_description = models.ForeignKey(
        ItemDescription, on_delete=models.PROTECT, blank=True, null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, blank=True, null=True)
    address = models.ForeignKey(
        ProfileAddress, on_delete=models.PROTECT, blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    cust_id_or_reg_no = models.CharField(
        max_length=250, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    outlet = models.CharField(max_length=255, blank=True, null=True)

    model = models.CharField(max_length=255, blank=True, null=True)
    varient = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    pickup_slot = models.DateTimeField(auto_now=False)
    item_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    employee_id = models.CharField(max_length=255, blank=True, null=True)
    referred_by = models.CharField(max_length=255, blank=True, null=True)

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

    deliverred_time = models.DateTimeField(blank=True, null=True)
    booking_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=BOOKED)

    class Meta:
        verbose_name = 'SERVICE'
        verbose_name_plural = 'SERVICE'


class Accessory(models.Model):

    BOOKED = 'Booked'
    DISPATCHED = 'Booked'
    OUT_FOR_DELIVERY = 'Contacted'
    DELIVERRED = 'Deliverred'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (BOOKED, 'Booked'),
        (DISPATCHED, 'Contacted'),
        (OUT_FOR_DELIVERY, 'Picked Up'),
        (DELIVERRED, 'Deliverred'),
        (CANCELLED, 'Cancelled')
    ]

    booking_id = models.ForeignKey(
        AppBooking, on_delete=models.PROTECT, blank=True, null=True)
    itemlist = models.ForeignKey(
        Itemlist, on_delete=models.PROTECT, blank=True, null=True)
    item_description = models.ForeignKey(
        ItemDescription, on_delete=models.PROTECT, blank=True, null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, blank=True, null=True)
    cust_id_or_reg_no = models.CharField(
        max_length=250, blank=True, null=True)
    address = models.ForeignKey(
        ProfileAddress, on_delete=models.PROTECT, blank=True, null=True)
    item_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    quantity = models.IntegerField(default=1, blank=True)

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

    deliverred_time = models.DateTimeField(blank=True, null=True)
    booking_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=BOOKED)

    class Meta:
        verbose_name = 'ACCESSORY'
        verbose_name_plural = 'ACCESSORY'


class Insurance(models.Model):

    ENQUIRED = 'Enquired'
    CONTACTED = 'Contacted'
    BOOKED = 'Booked'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (ENQUIRED, 'Enquired'),
        (CONTACTED, 'Contacted'),
        (BOOKED, 'Booked'),
        (CANCELLED, 'Cancelled')
    ]
    itemlist = models.ForeignKey(
        Itemlist, on_delete=models.PROTECT, blank=True, null=True)
    item_description = models.ForeignKey(
        ItemDescription, on_delete=models.PROTECT, blank=True, null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, blank=True, null=True)
    address = models.ForeignKey(
        ProfileAddress, on_delete=models.PROTECT, blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    registered_number = models.CharField(max_length=255, blank=True, null=True)
    registered_city = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    variant = models.CharField(max_length=255, blank=True, null=True)
    fuel = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.CharField(max_length=255, blank=True, null=True)
    policy_expire_date = models.DateField(blank=True, null=True)
    last_claim_status = models.CharField(max_length=255, blank=True, null=True)
    claim_bonus = models.CharField(max_length=255, blank=True, null=True)

    employee_id = models.CharField(max_length=255, blank=True, null=True)
    referred_by = models.CharField(max_length=255, blank=True, null=True)
    addons = models.CharField(max_length=255, blank=True, null=True)

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

    # booked_at = models.DateTimeField(blank=True, null=True)
    booking_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=ENQUIRED)

    class Meta:
        verbose_name = 'INSURANCE'
        verbose_name_plural = 'INSURANCE'


class UsedcarSellEnquiry(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    evaluation_type = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    scheduled_at = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    vehicle_model = models.CharField(max_length=255, blank=True, null=True)
    vehicle_number = models.CharField(max_length=255, blank=True, null=True)
    vehicle_variant = models.CharField(max_length=255, blank=True, null=True)
    year_of_registration = models.CharField(
        max_length=255, blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name = 'USED CAR - SELL'
        verbose_name_plural = 'USED CAR - SELL'


class Pricing(models.Model):
    ACTIVE = 'Active'
    INACTIVE = 'InActive'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'InActive'),
    ]
    channel = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name='channel_pricing')
    price = models.IntegerField(default=0, blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        verbose_name = 'SET ADVANCE'
        verbose_name_plural = 'SET ADVANCE'