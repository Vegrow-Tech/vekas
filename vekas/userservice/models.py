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

class Authentication(models.Model):
    token = models.CharField(max_length=256)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField(default=default_expiry_date)
