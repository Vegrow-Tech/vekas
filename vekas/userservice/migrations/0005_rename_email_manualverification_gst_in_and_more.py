# Generated by Django 4.2.11 on 2024-03-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userservice', '0004_alter_authentication_expiry_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manualverification',
            old_name='email',
            new_name='gst_in',
        ),
        migrations.RemoveField(
            model_name='manualverification',
            name='gstIn',
        ),
        migrations.RemoveField(
            model_name='manualverification',
            name='pan_number',
        ),
        migrations.RemoveField(
            model_name='manualverification',
            name='user_name',
        ),
        migrations.AddField(
            model_name='manualverification',
            name='business_ph_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='manualverification',
            name='pin_code',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='manualverification',
            name='state',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
