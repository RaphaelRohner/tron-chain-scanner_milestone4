from django.db import models


# Create your models here.
class Identifiers(models.Model):
    """
    A model to store all sorts of Tron identifiers in.
    """

    # DEFINING DROPDOWN VALUES
    CHOICES = (
        ('', 'Select identifier type'),
        ('Contract', 'Contract'),
        ('TRC10', 'TRC10 Token'),
        ('TRC20', 'TRC20 Token'),
        ('Wallet', 'Wallet Address'),
    )

    class Meta:
        verbose_name_plural = 'Identifiers'

    identifier_contract = models.CharField(max_length=40, null=False, blank=False, unique=True)  # noqa: E501
    identifier_name = models.CharField(max_length=50, null=False, blank=False, unique=True)  # noqa: E501
    # e.g. contract, token, address
    identifier_type = models.CharField(max_length=100, null=False, blank=False, choices=CHOICES)  # noqa: E501
    identifier_comment = models.CharField(max_length=250, null=False, blank=False)  # noqa: E501

    def __str__(self):
        return self.identifier_contract
