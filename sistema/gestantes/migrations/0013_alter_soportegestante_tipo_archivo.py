# Generated by Django 4.2.4 on 2023-09-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestantes', '0012_alter_soportegestante_tipo_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soportegestante',
            name='tipo_archivo',
            field=models.CharField(choices=[('IC', 'Inicio de control'), ('VH', 'VIH'), ('SF', 'Sifilis'), ('HC', 'Historia clinica')], max_length=2, verbose_name='Tipo archivo'),
        ),
    ]
