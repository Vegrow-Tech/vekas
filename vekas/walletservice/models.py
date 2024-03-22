from django.db import models
class Wallet(models.Model):
    user_id = models.BigIntegerField()
    created_on = models.BigIntegerField()