from django.db import models
# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Category(models.Model):
    CATEGORY_MODEL = 'models'
    CATEGORY_VARIENT = 'varients'
    CATEGORY_DETAIL = 'details'
    CATEGORY_USEDCAR = 'Used Cars'
    CATEGORY_THANKYOU = 'thankyou'

    CATEGORY_CHOICES = [
        (CATEGORY_MODEL, 'models'),
        (CATEGORY_VARIENT, 'varients'),
        (CATEGORY_DETAIL, 'details'),
        (CATEGORY_USEDCAR, 'Used Cars'),
        (CATEGORY_THANKYOU, 'thankyou')
    ]

    ACTIVE = 'Active'
    INACTIVE = 'Inactive'

    ACTIVE_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    ]

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    page_navigation = models.CharField(
        max_length=15, choices=CATEGORY_CHOICES, default=CATEGORY_MODEL)
    image = models.ImageField(
        upload_to='store/images')
    banners = models.JSONField(null=True, blank=True)
    search_keyword = models.CharField(max_length=255, null=True, blank=True)
    prefix_keyword = models.CharField(max_length=255, null=True, blank=True)
    position = models.IntegerField(null=True, blank=True, unique=True)
    active_status = models.CharField(
        max_length=15, choices=ACTIVE_CHOICES, default=ACTIVE)
    isActive = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'CHANNELS'
        verbose_name_plural = 'CHANNELS'



class Itemlist(models.Model):
    CATEGORY_MODEL = 'models'
    CATEGORY_VARIENT = 'varients'
    CATEGORY_DETAIL = 'details'
    CATEGORY_USEDCAR = 'Used Cars'
    CATEGORY_THANKYOU = 'thankyou'

    CATEGORY_CHOICES = [
        (CATEGORY_MODEL, 'models'),
        (CATEGORY_VARIENT, 'varients'),
        (CATEGORY_DETAIL, 'details'),
        (CATEGORY_USEDCAR, 'Used Cars'),
        (CATEGORY_THANKYOU, 'thankyou')
    ]
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    images = models.JSONField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='items')
    page_navigation = models.CharField(
        max_length=15, choices=CATEGORY_CHOICES, default=CATEGORY_MODEL)
    search_keyword = models.CharField(max_length=255, null=True, blank=True)
    promotions = models.ManyToManyField(Promotion, blank=True)
    isActive = models.BooleanField(default=True)
    product_link = models.JSONField(null=True,blank=True)
    brochure_link = models.JSONField(null=True,blank=True)
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'ITEMS'
        verbose_name_plural = 'ITEMS'



class ItemDescription(models.Model):

    CATEGORY_MODEL = 'models'
    CATEGORY_VARIENT = 'varients'
    CATEGORY_DETAIL = 'details'
    SERVICE_DETAIL = 'service details'
    CATEGORY_USEDCAR = 'used cars'
    CATEGORY_THANKYOU = 'thankyou'

    CATEGORY_CHOICES = [
        (CATEGORY_MODEL, 'models'),
        (CATEGORY_VARIENT, 'varients'),
        (CATEGORY_DETAIL, 'details'),
        (SERVICE_DETAIL, 'service details'),
        (CATEGORY_USEDCAR, 'used cars'),
        (CATEGORY_THANKYOU, 'thankyou')
    ]
    title_for_price = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255)
    ex_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    images = models.JSONField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    itemlist = models.ForeignKey(
        Itemlist, on_delete=models.PROTECT, related_name='itemlist')
    page_navigation = models.CharField(
        max_length=15, choices=CATEGORY_CHOICES, default=CATEGORY_MODEL)
    channel = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='channel_item_desc', null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'ITEM DESCRIPTION'
        verbose_name_plural = 'ITEM DESCRIPTION'



class ItemDescSpec(models.Model):
    item_desc = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, related_name='spec')
    item_spec = models.CharField(max_length=255)
    value = models.CharField(max_length=255)



    def __str__(self) -> str:
        return self.item_desc.title

    class Meta:
        ordering = ['item_desc']
        verbose_name = 'SPECIFICATIONS'
        verbose_name_plural = 'SPECIFICATIONS'


class Faqs(models.Model):

    model = models.ForeignKey(Itemlist, on_delete=models.DO_NOTHING, null=True, blank=True)
    question = models.TextField()
    answer = models.TextField()
    isActive = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'SET FAQ'+'S'
        verbose_name_plural = 'SET FAQ' + 'S'


from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry

from .models import ItemDescription

@registry.register_document
class ItemDescriptionDocument(Document):
    class Index:
        name = 'item_descriptions'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = ItemDescription
        fields = ['title']
