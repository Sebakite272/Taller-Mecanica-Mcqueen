# Generated by Django 4.0.5 on 2022-07-08 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_diagnostico_servicio_diagnosticos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('motivo', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=500)),
            ],
        ),
    ]
