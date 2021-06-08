from django.db import models


class Manufacturer(models.Model):
    manufacturer = models.CharField(
        max_length=20,
        null=True,
        blank=False,
    )
