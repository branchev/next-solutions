from django.db import models

from next_sol.vehicles.models.bg_reg import BGRegNumber
from .fuel_type import FuelType
from .manufacturer import Manufacturer
from .manufacturer_model import ManufacturerModel


class CurrentVehicleData(models.Model):
    engine_vol = models.FloatField(
        null=True,
        blank=False,
    )
    first_reg = models.CharField(
        max_length=10,
        null=True,
        blank=False,
    )

    bg_reg_number = models.ForeignKey(
        BGRegNumber,
        on_delete=models.CASCADE,
        null=True,
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        null=True,
    )
    manufacturer_model = models.ForeignKey(
        ManufacturerModel,
        on_delete=models.CASCADE,
        null=True,
    )
    fuel_type = models.ForeignKey(
        FuelType,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.manufacturer_model.man_model
