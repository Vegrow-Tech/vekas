from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.
# class Wallet(models.Model):
#     user_id = models.BigIntegerField()
#     created_on = models.BigIntegerField()

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
