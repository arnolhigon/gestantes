# Generated by Django 4.2.4 on 2023-09-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestantes', '0011_alter_soportegestante_soporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soportegestante',
            name='tipo_archivo',
            field=models.CharField(choices=[('IC', 'Inicio de control'), ('2', 'VIH'), ('3', 'Sifilis'), ('4', 'Historia clinica')], max_length=2, verbose_name='Tipo archivo'),
        ),
    ]
