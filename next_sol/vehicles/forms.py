from django import forms


class DateInputForm(forms.DateInput):
    input_type = 'date'


class RegisterForm(forms.Form):
    bg_reg_number = forms.CharField(
        label='BG Reg. Number',
        required=True,
        min_length=7,
        max_length=8,
    )
    manufacturer = forms.CharField(
        required=True,
        label='Manufacturer',
        max_length=20,
    )
    man_model = forms.CharField(
        required=True,
        label='Model',
        max_length=15,
    )
    # TODO CHOICE FIELD
    fuel_type = forms.CharField(
        required=True,
        label='Fuel Type',
        max_length=10,
    )
    engine_vol = forms.FloatField(
        required=True,
        label='Engine vol. (Liters)',
        min_value=0,
        max_value=7.5,
    )
    first_registration = forms.DateField(
        required=True,
        label='First Reg. Date',
        widget=DateInputForm,
    )


class SearchForm(forms.Form):
    key = forms.CharField(
        required=True,
        label="Type a text",
        max_length=30,
    )


class DeleteForm(forms.Form):
    bg_reg_number = forms.CharField(
        required=True,
        label="Type a Reg. Number",
        max_length=30,
    )
