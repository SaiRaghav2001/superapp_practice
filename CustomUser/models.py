from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Profile(models.Model):
    MEMBERSHIP_MEMBER = 'Member'
    MEMBERSHIP_GOLD = 'Gold'
    MEMBERSHIP_PLATINUM = 'Platinum'
    MEMBERSHIP_TITANIUM = 'Titanium'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_MEMBER, 'Member'),
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_PLATINUM, 'Platinum'),
        (MEMBERSHIP_TITANIUM, 'Titanium')
    ]

    ACTIVE = 'Active'
    INACTIVE = 'Inactive'

    ACTIVE_STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

    phone = models.CharField(max_length=255, null=True,
                             blank=True, unique=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)
    year_of_birth = models.IntegerField(null=True, blank=True)
    active_status = models.CharField(
        max_length=50, choices=ACTIVE_STATUS, default=ACTIVE)
    membership = models.CharField(
        max_length=25, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_MEMBER)
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name='user')
    verified_profile = models.BooleanField(default=False)
    pan_number = models.CharField(max_length=255, null=True, blank=True)
    app_version = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        verbose_name = 'USER PROFILE'
        verbose_name_plural = 'USER PROFILE'




class ProfileVerification(models.Model):

    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='pan_profile', null=True, blank=True)
    pan_number = models.CharField(max_length=255, null=True, blank=True)
    name_as_per_pan = models.CharField(max_length=100, null=True, blank=True)
    dob = models.CharField(max_length=50, null=True, blank=True)
    pan_image = models.ImageField(upload_to='store/images')

    verified_pan = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'PROFILE DOCUMENTS'
        verbose_name_plural = 'PROFILE DOCUMENTS'


