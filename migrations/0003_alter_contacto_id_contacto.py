# Generated by Django 4.0.5 on 2022-06-20 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contacto_mensaje_alter_contacto_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='id_contacto',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Contacto'),
        ),
    ]
