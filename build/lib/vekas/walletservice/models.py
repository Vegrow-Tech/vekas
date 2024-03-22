from datetime import datetime
from django.db import models
from vekas.userservice.models import Customer
from uuid import uuid4
from django.utils import timezone


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, default=str(uuid4))
    created_on = models.DateTimeField(default=timezone.now)


# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    amount = models.FloatField(default=0)


class WalletTransactions(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    transaction_type = models.CharField(max_length=10, null=False, blank=False)
    amount = models.FloatField(default=0)
    expiration = models.IntegerField(default=None)
    transaction_id = models.CharField(max_length=100)


class WalletTransactionsMetaData(models.Model):
    wallet_transaction = models.ForeignKey(WalletTransactions, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    transfer_type = models.IntegerField()
    transfer_to_id = models.IntegerField()



from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#
# class Customer(User):
#     user_id = models.CharField(max_length=50, null=False, blank=False, unique=True,db_index=True)
#     created_on = models.BigIntegerField()
#     is_archived = models.BooleanField(default=False)
#     validated = models.BooleanField(default=False)
#
#
# class Authentication(models.Model):
#     token = models.CharField(max_length=50)
#     expiry_date = models.BigIntegerField()
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)


# class Validation(models.Model):
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     expiry_date = models.BigIntegerField()


# class CustomerDetails(models.Model):
#     cv_link = models.CharField(max_length=125, null=True, blank=True)
#     like_to_work = models.BooleanField(null=True, blank=True)
#     cover_letter = models.TextField()
#     web_address = models.CharField(max_length=256)
#     ip_address = models.CharField(max_length=126)
#     lat = models.CharField(max_length=126)
#     long = models.CharField(max_length=126)
#     last_active = models.BooleanField(null=True, blank=True)
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)


# class ReviewedDetails(models.Model):
#     reviewed_by = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reviewed_by")
#     reviewed_whom = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reviewed_whom")
#     reviewed_on = models.BigIntegerField(null=False)


# class Comments(models.Model):
#     comment_by = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="comment_by")
#     comment_whom = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="comment_whom")
#     comment_on = models.BigIntegerField(null=False)
#     comment = models.TextField(null=False, blank=False)


# class Rating(models.Model):
#     rating_by = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="rating_by")
#     rating_whom = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="rating_whom")
#     rating_on = models.BigIntegerField(null=False)
#     rating = models.IntegerField(null=False)


# class AVGRating(models.Model):
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     avg_rating = models.FloatField(null=False)
