from django.db import models


# Create your models here.
class Wallet(models.Model):
    """
    A model to store the wallet public key and an additional friendly name.
    """
    wallet_pk = models.CharField(max_length=40, null=False, blank=False)
    wallet_name = models.CharField(max_length=50, null=True, blank=True)  # noqa: DJ01, E501

    def __str__(self):
        return self.wallet_pk


class WalletPay(models.Model):
    """
    A model to store a users crypto payments and payment dates
    to calculate available usage time.
    """
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_amount = models.IntegerField(null=False, blank=False)
    payment_currency = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.wallet


class walletAdd(models.Model):
    """
    A model to store additional wallets
    with their public key and an additional friendly name.
    """
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    add_wallet_pk = models.CharField(max_length=40, null=False, blank=False)  # noqa: E501
    add_wallet_name = models.CharField(max_length=50, null=True, blank=True)  # noqa: DJ01, E501

    def __str__(self):
        return self.wallet
