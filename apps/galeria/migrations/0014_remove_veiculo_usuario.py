# Generated by Django 4.2.1 on 2023-08-17 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0013_alter_veiculo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='usuario',
        ),
    ]