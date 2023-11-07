# Generated by Django 4.2.4 on 2023-10-09 20:40

from django.db import migrations, models
import gestantes.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestantes', '0019_remove_carguemensual_nombre_excel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carguemensual',
            name='soporte_excel',
            field=models.FileField(upload_to='', validators=[gestantes.models.validate_excel_file_extension], verbose_name='Soporte Excel'),
        ),
    ]