from django.contrib import admin

from next_sol.vehicles.models import \
    BGRegNumber, \
    Manufacturer, \
    ManufacturerModel, \
    CurrentVehicleData, \
    FuelType

admin.site.register(BGRegNumber)
admin.site.register(Manufacturer)
admin.site.register(ManufacturerModel)
admin.site.register(CurrentVehicleData)
admin.site.register(FuelType)

