# Generated by Django 4.2.1 on 2023-06-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_alter_veiculo_motor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.CharField(choices=[('HONDA', 'Honda'), ('YAMAHA', 'Yamaha'), ('BMW', 'BMW'), ('AUDI', 'Audi'), ('FIAT', 'Fiat'), ('CHEVROLET', 'Chevrolet'), ('VOLVO', 'Volvo'), ('IVECO', 'Iveco'), ('DUCATI', 'Ducati'), ('HYUNDAI', 'Hyundai'), ('TRIUMPH', 'Triumph'), ('FORD', 'Ford'), ('RENAULT', 'Renault'), ('JEEP', 'Jeep'), ('SUZUKI', 'Suzuki')], default='', max_length=30),
        ),
    ]
