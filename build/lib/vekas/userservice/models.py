from django.db import models

from vekas.utils.utility_functions import default_expiry_date


class Customer(models.Model):
    name = models.CharField(db_index=True, max_length=256, null=True, blank=True)
    language = models.CharField(max_length=20, default='en')
    phone_number = models.CharField(db_index=True, max_length=15, null=True, blank=True)
    velynk_customer_id = models.BigIntegerField()
    user_type = models.CharField(db_index=True, max_length=256, null=True, blank=True)
    created_on = models.BigIntegerField()
    is_archived = models.BooleanField(default=False)
    referral_code = models.CharField(db_index=True, max_length=256, unique=True)


class Authentication(models.Model):
    token = models.CharField(max_length=256)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField(default=default_expiry_date)


class Referral(models.Model):
    referred_to = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="referred_to")
    referred_by = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="referred_by")
    created_on = models.DateTimeField(auto_now_add=True)


class Lead(models.Model):
    phone_number = models.CharField(max_length=100, unique=True)
    referred_by = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
