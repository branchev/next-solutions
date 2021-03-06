# Generated by Django 3.2.4 on 2021-06-06 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManufacturerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('man_model', models.CharField(max_length=20, null=True)),
                ('fuel_type', models.CharField(max_length=10, null=True)),
                ('engine_vol', models.CharField(max_length=5, null=True)),
                ('first_reg', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BGRegNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_reg_number', models.CharField(max_length=10, unique=True)),
                ('man_model', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.manufacturermodel')),
                ('manufacturer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.manufacturer')),
            ],
        ),
    ]
