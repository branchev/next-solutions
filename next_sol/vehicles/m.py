from django.db import models


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=20, null=True)


class ManufacturerModel(models.Model):
    man_model = models.CharField(max_length=20, null=True)
    fuel_type = models.CharField(max_length=10, null=True)
    engine_vol = models.CharField(max_length=5, null=True)
    first_reg = models.CharField(max_length=10, null=True)


class BGRegNumber(models.Model):
    bg_reg_number = models.CharField(max_length=10, unique=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    man_model = models.ForeignKey(ManufacturerModel, on_delete=models.CASCADE, null=True)
