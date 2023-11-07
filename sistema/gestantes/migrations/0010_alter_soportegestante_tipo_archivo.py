# Generated by Django 4.2.4 on 2023-08-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestantes', '0009_alter_soportegestante_tipo_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soportegestante',
            name='tipo_archivo',
            field=models.CharField(choices=[('1', 'Inicio de control'), ('2', 'VIH'), ('3', 'Sifilis'), ('4', 'Historia clinica')], max_length=2, verbose_name='Tipo archivo'),
        ),
    ]
