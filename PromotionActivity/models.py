from django.db import models
from ProductData.models import *
from CustomUser.models import *
# Create your models here.
class Alerts(models.Model):

    title = models.CharField(max_length=255, null=True, blank=True)
    about = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    action = models.CharField(max_length=50, null=True, blank=True)
    page_navigation = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'ALERTS'
        verbose_name_plural = 'ALERTS'


class Promotions(models.Model):
    title = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'PROMOTIONS'
        verbose_name_plural = 'PROMOTIONS'


class Banner(models.Model):

    CATEGORY_TEXT = 'text'
    CATEGORY_IMAGE = 'image'

    CATEGORY_CHOICES = [
        (CATEGORY_TEXT, 'text'),
        (CATEGORY_IMAGE, 'image'),
    ]

    promotion_type = models.CharField(
        max_length=15, choices=CATEGORY_CHOICES, default=CATEGORY_IMAGE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store/images', null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    page_navigation = models.CharField(max_length=255, null=True, blank=True)
    position = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'BANNERS'
        verbose_name_plural = 'BANNERS'



class FeaturedItem(models.Model):
    promotion = models.ForeignKey(
        Promotions, on_delete=models.PROTECT, related_name='promotion', null=True, blank=True)
    promoted_item = models.ForeignKey(
        ItemDescription, on_delete=models.PROTECT, related_name='promoted_item', null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    position = models.PositiveSmallIntegerField(null=True, blank=True)
    page_navigation = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'FEATURED ITEMS'
        verbose_name_plural = 'FEATURED ITEMS'



