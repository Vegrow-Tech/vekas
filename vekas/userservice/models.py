from django.db import models

class Customer(models.Model):
    name = models.CharField(db_index=True, max_length=256, null=True, blank=True)
    language = models.CharField(max_length=20, default='en')
    phone_number = models.CharField(db_index=True, max_length=15, null=True, blank=True)
    velynk_customer_id = models.BigIntegerField(null=True, blank=True)
    customer_type = models.CharField(db_index=True, max_length=256, null=True, blank=True)
    created_on = models.BigIntegerField()
    is_archived = models.BooleanField(default=False)
    is_kyc_verified = models.BooleanField(default=False)
    kyc_verification_type = models.CharField(max_length=50, null=True, blank=True)  

class Authentication(models.Model):
    token = models.CharField(max_length=256)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()

class AadharVerification(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    aadhar_number = models.CharField(max_length=20)
    aadhar_details = models.TextField()
    created_on = models.BigIntegerField()

class PanVerification(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pan_number = models.CharField(max_length=20)
    pan_details = models.TextField()
    created_on = models.BigIntegerField()    

class ManualVerification(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=256)
    address = models.CharField(max_length=1024)
    city = models.CharField(max_length=64)
    state =  models.CharField(max_length=64),
    pin_code =  models.CharField(max_length=25),
    business_ph_number =  models.CharField(max_length=20),
    gst_in = models.CharField(max_length=256)
    signature =  models.CharField(max_length=256)
    created_on = models.BigIntegerField()

