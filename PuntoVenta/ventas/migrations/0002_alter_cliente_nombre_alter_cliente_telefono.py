# Generated by Django 5.0.2 on 2024-02-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=200, null=True),
        ),
    ]