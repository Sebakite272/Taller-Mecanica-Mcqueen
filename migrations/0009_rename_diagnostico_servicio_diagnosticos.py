# Generated by Django 4.0.5 on 2022-07-07 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_atencion_servicio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='diagnostico',
            new_name='diagnosticos',
        ),
    ]
