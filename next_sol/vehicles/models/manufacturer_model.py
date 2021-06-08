from django.db import models

from next_sol.vehicles.models import Manufacturer


class ManufacturerModel(models.Model):
    man_model = models.CharField(
        max_length=15,
        null=True,
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        null=True,
    )
