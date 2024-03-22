# Generated by Django 4.2.11 on 2024-03-22 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userservice', '0002_alter_authentication_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(default='<function uuid4 at 0x10b08dd30>', max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userservice.customer')),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('transaction_type', models.CharField(max_length=10)),
                ('amount', models.FloatField(default=0)),
                ('expiration', models.IntegerField(default=None)),
                ('transaction_id', models.CharField(max_length=100)),
                ('transaction_message', models.CharField(max_length=512)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='walletservice.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransactionsMetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('transfer_type', models.IntegerField()),
                ('transfer_to_id', models.IntegerField()),
                ('wallet_transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='walletservice.wallettransactions')),
            ],
        ),
    ]
