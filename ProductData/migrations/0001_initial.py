# Generated by Django 5.1.3 on 2024-11-28 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('page_navigation', models.CharField(choices=[('models', 'models'), ('varients', 'varients'), ('details', 'details'), ('Used Cars', 'Used Cars'), ('thankyou', 'thankyou')], default='models', max_length=15)),
                ('image', models.ImageField(upload_to='store/images')),
                ('banners', models.JSONField(blank=True, null=True)),
                ('search_keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('prefix_keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.IntegerField(blank=True, null=True, unique=True)),
                ('active_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=15)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'CHANNELS',
                'verbose_name_plural': 'CHANNELS',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_for_price', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(max_length=255)),
                ('ex_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('page_navigation', models.CharField(choices=[('models', 'models'), ('varients', 'varients'), ('details', 'details'), ('service details', 'service details'), ('used cars', 'used cars'), ('thankyou', 'thankyou')], default='models', max_length=15)),
                ('isActive', models.BooleanField(default=True)),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='channel_item_desc', to='ProductData.category')),
            ],
            options={
                'verbose_name': 'ITEM DESCRIPTION',
                'verbose_name_plural': 'ITEM DESCRIPTION',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ItemDescSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_spec', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('item_desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec', to='ProductData.itemdescription')),
            ],
            options={
                'verbose_name': 'SPECIFICATIONS',
                'verbose_name_plural': 'SPECIFICATIONS',
                'ordering': ['item_desc'],
            },
        ),
        migrations.CreateModel(
            name='Itemlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('images', models.JSONField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('page_navigation', models.CharField(choices=[('models', 'models'), ('varients', 'varients'), ('details', 'details'), ('Used Cars', 'Used Cars'), ('thankyou', 'thankyou')], default='models', max_length=15)),
                ('search_keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('product_link', models.JSONField(blank=True, null=True)),
                ('brochure_link', models.JSONField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='ProductData.category')),
                ('promotions', models.ManyToManyField(blank=True, to='ProductData.promotion')),
            ],
            options={
                'verbose_name': 'ITEMS',
                'verbose_name_plural': 'ITEMS',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='itemdescription',
            name='itemlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itemlist', to='ProductData.itemlist'),
        ),
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('isActive', models.BooleanField(default=True)),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ProductData.itemlist')),
            ],
            options={
                'verbose_name': 'SET FAQS',
                'verbose_name_plural': 'SET FAQS',
            },
        ),
    ]
