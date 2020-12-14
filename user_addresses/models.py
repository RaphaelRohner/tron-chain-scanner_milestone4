from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


# Create your models here.
class UserAddresses(models.Model):
    """
    A user profile model for administrating
    additional delivery addresses.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_full_name = models.CharField(max_length=50, null=True, blank=True)  # noqa: DJ01, E501
    additional_phone_number = models.CharField(max_length=20, null=True, blank=True)  # noqa: DJ01, E501
    additional_street_address1 = models.CharField(max_length=80, null=True, blank=True)  # noqa: DJ01, E501
    additional_street_address2 = models.CharField(max_length=80, null=True, blank=True)  # noqa: DJ01, E501
    additional_town_or_city = models.CharField(max_length=40, null=True, blank=True)  # noqa: DJ01, E501
    additional_county = models.CharField(max_length=80, null=True, blank=True)  # noqa: DJ01, E501
    additional_postcode = models.CharField(max_length=20, null=True, blank=True)  # noqa: DJ01, E501
    additional_country = CountryField(blank_label='Country', null=True, blank=True)  # noqa: DJ01, E501

    def __str__(self):
        return self.user.username  # pylint: disable=maybe-no-member
