# Generated by Django 4.2.1 on 2023-08-17 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0012_veiculo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
