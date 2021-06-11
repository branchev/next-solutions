from django.shortcuts import render, redirect

from next_sol.vehicles.forms import RegisterForm, DateInputForm, SearchForm, DeleteForm
from next_sol.vehicles.models import BGRegNumber, ManufacturerModel, Manufacturer, CurrentVehicleData, FuelType


def index(request):
    context = {
        'register_form': RegisterForm(),
        'date_input_form': DateInputForm(),
        'search_form': SearchForm(),
        'delete_form': DeleteForm(),
    }
    return render(request, 'index.html', context)


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
        manufacturer_model=new_manufacturer_model,
        fuel_type=new_fuel_type,
    )
    new_current_vehicle_data.save()

    return redirect('/')


def list_vehicles(request):
    context = {
        'current_model': CurrentVehicleData.objects.all(),
        'bg_regs': BGRegNumber.objects.all(),
        'fuel_type': FuelType.objects.all(),
        'manufacturer': Manufacturer.objects.all(),
        'man_model': ManufacturerModel.objects.all(),
    }

    return render(request, 'list_vehicles.html', context)


def search_vehicles(request):
    # TODO CONVERT ALL DIGITS AND LETTERS TO UPPER OR LOWER CASE FOR SEARCHING
    key_word = request.POST['key']

    regs = set([reg for reg in BGRegNumber.objects.all() if key_word in reg.bg_reg_number])
    manufacturers = set([m for m in Manufacturer.objects.all() if key_word in m.manufacturer])
    m_models = set([mod for mod in ManufacturerModel.objects.all() if key_word in mod.man_model])

    results = []

    for car in CurrentVehicleData.objects.all():
        if car.bg_reg_number in regs:
            results.append(car)
        elif car.manufacturer in manufacturers:
            results.append(car)
        elif car.manufacturer_model in m_models:
            results.append(car)
        elif key_word in str(CurrentVehicleData.engine_vol):
            results.append(car)
        elif key_word in str(CurrentVehicleData.first_reg):
            results.append(car)

    context = {
        'current_model': CurrentVehicleData.objects.all(),
        'bg_regs': BGRegNumber.objects.all(),
        'fuel_type': FuelType.objects.all(),
        'manufacturer': Manufacturer.objects.all(),
        'man_model': ManufacturerModel.objects.all(),

        'result': results,
    }

    return render(request, 'search.html', context)


def delete_vehicle(request):
    reg_number = request.POST['bg_reg_number']

    searched_reg = BGRegNumber.objects. \
        filter(bg_reg_number=reg_number). \
        first()
    if searched_reg:
        searched_reg.delete()
    return redirect('/')
