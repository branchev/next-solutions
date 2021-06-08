from django.shortcuts import render, redirect

from next_sol.vehicles.models import BGRegNumber, ManufacturerModel, Manufacturer, CurrentVehicleData, FuelType


def index(request):
    return render(request, 'index.html')


def register_vehicle(request):
    reg_number = request.POST['bg_reg_number']
    supplier = request.POST['manufacturer']
    manufacturing_model = request.POST['man_model']
    type_of_fuel = request.POST['fuel_type']
    vol_of_engine = request.POST['engine_vol']
    date_first_registration = request.POST['first_registration']

    new_reg = BGRegNumber.objects. \
        filter(bg_reg_number=reg_number). \
        first()
    if not new_reg:
        new_reg = BGRegNumber(bg_reg_number=reg_number)
        new_reg.save()
    else:
        return redirect('/')

    new_manufacturer = Manufacturer.objects. \
        filter(manufacturer=supplier). \
        first()
    if not new_manufacturer:
        new_manufacturer = Manufacturer(manufacturer=supplier)
        new_manufacturer.save()

    new_manufacturer_model = ManufacturerModel.objects. \
        filter(man_model=manufacturing_model). \
        first()
    if not new_manufacturer_model:
        new_manufacturer_model = ManufacturerModel(
            man_model=manufacturing_model,
            manufacturer=new_manufacturer,
        )
        new_manufacturer_model.save()

    new_fuel_type = FuelType.objects \
        .filter(fuel_type=type_of_fuel) \
        .first()
    if not new_fuel_type:
        new_fuel_type = FuelType(fuel_type=type_of_fuel)
        new_fuel_type.save()

    new_current_vehicle_data = CurrentVehicleData(
        engine_vol=vol_of_engine,
        first_reg=date_first_registration,
        bg_reg_number=new_reg,
        manufacturer=new_manufacturer,
        manufacturer_model=new_manufacturer_model
    )
    new_current_vehicle_data.save()

    return redirect('/')


def list_vehicles(request):
    context = {
        "vehicles": BGRegNumber.objects.all(),
        "models": ManufacturerModel.objects.all(),
        "manufacturers": Manufacturer.objects.all(),

        # "current_manufacturer": lambda x: Manufacturer.objects.filter(id=x).first(),

    }
    return render(request, 'list_vehicles.html', context)
