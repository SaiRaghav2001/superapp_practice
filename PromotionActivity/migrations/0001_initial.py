# Generated by Django 5.1.3 on 2024-11-28 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProductData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('about', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('action', models.CharField(blank=True, max_length=50, null=True)),
                ('page_navigation', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'ALERTS',
                'verbose_name_plural': 'ALERTS',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_type', models.CharField(choices=[('text', 'text'), ('image', 'image')], default='image', max_length=15)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='store/images')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('page_navigation', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'BANNERS',
                'verbose_name_plural': 'BANNERS',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('position', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'PROMOTIONS',
                'verbose_name_plural': 'PROMOTIONS',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='FeaturedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('page_navigation', models.CharField(blank=True, max_length=255, null=True)),
                ('promoted_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promoted_item', to='ProductData.itemdescription')),
                ('promotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promotion', to='PromotionActivity.promotions')),
            ],
            options={
                'verbose_name': 'FEATURED ITEMS',
                'verbose_name_plural': 'FEATURED ITEMS',
            },
        ),
    ]
