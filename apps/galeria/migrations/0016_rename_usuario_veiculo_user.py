# Generated by Django 4.2.1 on 2023-08-17 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0015_veiculo_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='usuario',
            new_name='user',
        ),
    ]
