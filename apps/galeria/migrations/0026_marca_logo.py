# Generated by Django 4.2.2 on 2023-08-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0025_remove_marca_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='logo',
            field=models.ImageField(blank=True, default='', upload_to='logos'),
        ),
    ]