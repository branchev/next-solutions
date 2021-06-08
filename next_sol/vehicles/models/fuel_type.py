from django.db import models


class FuelType(models.Model):
    GASOLINE_CHOICE = "Gasoline"
    DIESEL_CHOICE = "Diesel"
    LPG_CHOICE = "LPG"
    METHANE_CHOICE = "Methane"
    ELECTRICAL_CHOICE = "Electrical"
    NAME_CHOICES = (
        (GASOLINE_CHOICE, 'Gasoline'),
        (DIESEL_CHOICE, "Diesel"),
        (LPG_CHOICE, "LPG"),
        (METHANE_CHOICE, "Methane"),
        (ELECTRICAL_CHOICE, "Electrical"),
    )

    fuel_type = models.CharField(
        max_length=10,
        null=True,
        blank=False,
        choices=NAME_CHOICES,
    )

