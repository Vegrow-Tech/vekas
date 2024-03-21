from django.db import models

class AppCustomer(models.Model):
    first_name = models.CharField(db_index=True, max_length=256, null=True, blank=True)
    last_name = models.CharField(db_index=True, max_length=256, null=True, blank=True)
    language = models.CharField(max_length=20, default='en')
    phone_number = models.CharField(db_index=True, max_length=15, null=True, blank=True)
    velynk_customer_id = models.BigIntegerField()


class Authentication(models.Model):
    token = models.CharField(max_length=256)
    user = models.ForeignKey(AppCustomer, on_delete=models.CASCADE)