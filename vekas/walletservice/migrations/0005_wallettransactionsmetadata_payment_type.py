# Generated by Django 4.2.11 on 2024-03-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walletservice', '0004_wallettransactions_is_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallettransactionsmetadata',
            name='payment_type',
            field=models.CharField(default=None, max_length=256),
        ),
    ]