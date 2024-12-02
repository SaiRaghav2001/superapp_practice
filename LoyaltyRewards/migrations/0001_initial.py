# Generated by Django 5.1.3 on 2024-11-28 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BookingInfo', '0001_initial'),
        ('CollectionInfo', '0001_initial'),
        ('CustomUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoyaltiEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Member', 'Member'), ('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Titanium', 'Titanium'), ('Inaugural', 'Inaugural')], default='Member', max_length=50)),
                ('points_add_per_100', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('points_upgrade', models.IntegerField(blank=True, default=0, null=True)),
                ('time_of_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'LOYALTY CLAUSE',
                'verbose_name_plural': 'LOYALTY CLAUSE',
            },
        ),
        migrations.CreateModel(
            name='Loyalti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_earned_points', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('balance_points', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('last_updated_points', models.DateTimeField(auto_now=True)),
                ('business_turnover', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('inaugural_points', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('inaugural_points_eligible', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_loyalti', to='CustomUser.profile', unique=True)),
            ],
            options={
                'verbose_name': 'LOYALTY SUMMARY',
                'verbose_name_plural': 'LOYALTY SUMMARY',
            },
        ),
        migrations.CreateModel(
            name='LoyaltiTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('transaction_number', models.CharField(blank=True, max_length=250, null=True)),
                ('points_used', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('added_points', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('status', models.CharField(choices=[('Success', 'Success'), ('Failed', 'Failed')], default=None, max_length=50)),
                ('time_of_transaction', models.DateTimeField(auto_now=True)),
                ('transaction_type', models.CharField(choices=[('Add', 'Add'), ('Redeem', 'Redeem')], default=None, max_length=50)),
                ('purpose', models.TextField(blank=True, null=True)),
                ('app_booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BookingInfo.appbooking')),
                ('loyalti', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='LoyaltyRewards.loyalti')),
                ('payment_request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CollectionInfo.paymentrequest')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_loyalti_transaction', to='CustomUser.profile')),
            ],
            options={
                'verbose_name': 'LOYALTY TRANSACTIONS',
                'verbose_name_plural': 'LOYALTY TRANSACTIONS',
            },
        ),
    ]