# Generated by Django 4.2.4 on 2023-09-01 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestantes', '0013_alter_soportegestante_tipo_archivo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soportegestante',
            old_name='tipo_archivo',
            new_name='tipo_arch',
        ),
    ]
