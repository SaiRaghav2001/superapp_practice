from django.db import models
from CustomUser.models import Profile

# Create your models here.


class PaymentMode(models.Model):
    ACTIVE = 'Active'
    INACTIVE = 'InActive'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'InActive'),
    ]
    payment_mode_name = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        verbose_name = 'PAYMENT MODE'
        verbose_name_plural = 'PAYMENT MODE'


class PaymentModes(models.Model):
	
	ACTIVE = 'Active'
	INACTIVE = 'InActive'

	STATUS_CHOICES = [
			(ACTIVE, 'Active'),
			(INACTIVE, 'InActive'),
	]

	PHONEPAY = 'PHONEPAY'
	GPAY = 'GOOGLEPAY'
	CRED = 'CRED'
	PAYTM = 'PAYTM'
	UPI = 'UPI'

	MODES = [
			(PHONEPAY , 'PHONEPAY'),
			(GPAY , 'GOOGLEPAY'),
			(CRED , 'CRED'),
			(PAYTM , 'PAYTM'),
			(UPI , 'UPI')
	]
	
	paymentMode = models.CharField(max_length=255, blank=True, null=True, choices=MODES)
	aggregatorName = models.CharField(max_length=255, blank=True, null=True)
	aggregatorext = models.CharField(max_length=255, blank=True, null=True)
	aggregatorIcon = models.ImageField(blank=True, null=True, upload_to='media/paymentMode/')
	status = models.CharField(max_length=255,blank=True, null=True, choices=STATUS_CHOICES)

	class Meta:
		verbose_name = "AVAILABLE MODES"
		verbose_name_plural = "AVAILABLE MODES"

class UserOwnedModes(models.Model):

	ACTIVE = 'Active'
	INACTIVE = 'InActive'

	STATUS_CHOICES = [
			(ACTIVE, 'Active'),
			(INACTIVE, 'InActive'),
	]
	

	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	mode = models.ForeignKey(PaymentModes, on_delete=models.CASCADE)
	modeParams = models.JSONField(blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	last_used = models.DateTimeField(blank=True, null=True)
	status = models.CharField(max_length=255,blank=True, null=True, choices=STATUS_CHOICES)

	class Meta:
		verbose_name = "USER OWNED"
		verbose_name_plural = "USER OWNED"


class PayuBanksInfo(models.Model):
    # NETBANK = 'Netbank'
    # EMI = 'Emi'

    # STATUS_CHOICES = [
    #     (NETBANK, 'Netbank'),
    #     (EMI, 'Emi'),
    # ]
    bankName = models.CharField(max_length=250, blank=True, null=True)
    bankCode = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    # source = models.CharField(
    #     max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'PAYU BANK INFO'
        verbose_name_plural = 'PAYU BANK INFO'