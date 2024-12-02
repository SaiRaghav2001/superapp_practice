from django.db import models
from CustomUser.models import Profile
from ProductData.models import * 

# Create your models here.
class ProfileAddress(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile_address')
    type_of_address = models.CharField(max_length=255, null=True, blank=True)
    door_no = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1, null=True, blank=True)

    class Meta:
        verbose_name = 'PROFILE ADDRESS'
        verbose_name_plural = 'PROFILE ADDRESS'

    def __str__(self) -> str:
        return str(self.profile)
    
class ProfileActivity(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='activity_profile', null=True, blank=True, default=None)
    type = models.CharField(max_length=255, null=True, blank=True)
    instance = models.CharField(max_length=255, null=True, blank=True)
    search_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'PROFILE ANALYTICS'
        verbose_name_plural = 'PROFILE ANALYTICS'


class Enquirylog(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile_log', null=True, blank=True, default=None)
    profile_address = models.CharField(max_length=255, null=True, blank=True)

    mobile = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    
    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)

    enquire_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    scheduled = models.DateTimeField(auto_now=True, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    item_description = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    type_of_enq = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    list = models.CharField(max_length=255, null=True, blank=True)
    detail = models.CharField(max_length=255, null=True, blank=True)

    remarks = models.TextField(null=True, blank=True)
    kmdriven = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = 'ENQUIRY LOG'
        verbose_name_plural = 'ENQUIRY LOGS'


class ProfileSearch(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='profile_search', default=None)
    keyword = models.CharField(max_length=255)
    search_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'PROFILE SEARCH'
        verbose_name_plural = 'PROFILE SEARCH'



class Wishlist(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='wishlist_profile')
    item = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, related_name='profile_item')

    class Meta:
        unique_together = [['profile', 'item']]
        verbose_name = 'WISHLIST'
        verbose_name_plural = 'WISHLIST'

class ProfileFbtoken(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile_fb')
    type_of_token = models.CharField(max_length=255, null=True, blank=True)
    device_name = models.CharField(max_length=255, null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1, null=True, blank=True)

    class Meta:
        verbose_name = 'FB TOKENS'
        verbose_name_plural = 'FB TOKENS'


class ProfileNoticationPreference(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='profile_preference')
    type_of_notification = models.CharField(
        max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1, null=True, blank=True)

    class Meta:
        verbose_name = 'NOTIFICATION PREFERENCE'
        verbose_name_plural = 'NOTIFICATION PREFERENCE'


class ProfileAoi(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='profile_aoi')
    type = models.CharField(max_length=255, null=True, blank=True)
    interest = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'PROFILE AOI'
        verbose_name_plural = 'PROFILE AOI'