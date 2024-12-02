from django.db import models
from ProductData.models import *
# Create your models here.
class AwardsAndAchievements(models.Model):

    description = models.TextField()
    image = models.URLField(max_length=500, blank=True, null=True)
    classname = models.CharField(max_length=250, blank=True, null=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'AWARD AND ACHIEVEMENT'
        verbose_name_plural = 'AWARDS AND ACHIEVEMENTS'

class City(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'OUTLET CITY'
        verbose_name_plural = 'OUTLET CITY'



class Outlet(models.Model):
    SHOWROOM = 'Showroom'
    TRUEVALUE = 'Truevalue'
    WORKSHOP = 'Workshop'
    COMMERCIAL = 'Commercial'

    STATUS_CHOICES = [
        (SHOWROOM, 'Showroom'),
        (TRUEVALUE, 'Truevalue'),
        (WORKSHOP, 'Workshop'),
        (COMMERCIAL, 'Commercial'),
    ]
    channel = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name='channel')
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, blank=True, null=True, related_name='city')
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=SHOWROOM)
    sap_outlet_name = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'OUTLET LOCATION'
        verbose_name_plural = 'OUTLET LOCATION'


class TrueValueLocation(models.Model):

    city = models.ForeignKey(
        City, on_delete=models.CASCADE, blank=True, null=True, related_name='tv_loc')
    branch = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, null=True, blank=True)
    phone  =  models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    google_map_link = models.URLField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'TRUEVALUE LOCATION'
        verbose_name_plural = 'TRUEVALUE LOCATIONS'



class Reviews(models.Model):

    NATIVE = 'Native'
    WEB = 'Web'
    OTHER = 'Other'

    STATUS_CHOICES = [
        (NATIVE, 'Native'),
        (WEB, 'Web'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=250, blank=True, null=True)
    customer_review = models.TextField()
    title = models.CharField(max_length=250, blank=True, null=True)
    thumbnail_img_link = models.URLField(max_length=500, blank=True, null=True)
    vehicle_review_link = models.URLField(max_length=500, blank=True, null=True)
    platform = models.CharField(max_length=250, choices=STATUS_CHOICES, default=OTHER)
    isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'REVIEWS'
        verbose_name_plural = 'REVIEWS'

    

class TermsConditions(models.Model):
    charges_term = models.TextField(max_length=1000, default=None, blank=True, null=True)
    charges_more_term = models.TextField(max_length=1000, default=None, blank=True, null=True)
    declarations_term = models.TextField(max_length=1000, default=None, blank=True, null=True)
    booking_advance_note = models.TextField(max_length=1000, default=None, blank=True, null=True)
    loyalty_terms = models.TextField(max_length=1000, default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'TERMS AND CONDITIONS'
        verbose_name_plural = 'TERMS AND CONDITIONS'


class AppVersion(models.Model):
    version_name = models.CharField(max_length=250, blank=True, null=True)
    version_description = models.CharField(
        max_length=250, blank=True, null=True)
    version_number = models.CharField(max_length=250, blank=True, null=True)
    version_notes = models.CharField(max_length=250, blank=True, null=True)
    version_remarks = models.CharField(max_length=250, blank=True, null=True)
    version_status = models.CharField(max_length=250, blank=True, null=True)
    maintenance_mode = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'APP VERSIONS'
        verbose_name_plural = 'APP VERSIONS'

class RTO(models.Model):
    display_order = models.CharField(max_length=255, blank=True, null=True)
    is_popular = models.CharField(max_length=255, blank=True, null=True)
    rto_code = models.CharField(max_length=255, blank=True, null=True)
    rto_id = models.CharField(max_length=255, blank=True, null=True)
    rto_name = models.CharField(max_length=255, blank=True, null=True)