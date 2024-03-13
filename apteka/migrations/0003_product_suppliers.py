# Generated by Django 5.0.2 on 2024-02-29 02:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apteka', '0002_sklad'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='suppliers',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='apteka.suppliers', verbose_name='Поставщик'),
        ),
    ]
