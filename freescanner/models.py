from django.db import models


# Create your models here.
class Identifiers(models.Model):
    """
    A model to store all sorts of Tron identifiers in.
    """

    class Meta:
        verbose_name_plural = 'Identifiers'

    identifier_id = models.CharField(max_length=40, null=False, blank=False)
    identifier_name = models.CharField(max_length=50, null=False, blank=False)
    # e.g. contract, token, address
    identifier_type = models.CharField(max_length=30, null=False, blank=False)
    identifier_comment = models.CharField(max_length=250, null=False, blank=False)  # noqa: E501

    def __str__(self):
        return self.identifier_id
