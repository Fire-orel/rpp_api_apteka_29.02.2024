# Generated by Django 5.0.2 on 2024-03-21 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apteka', '0005_remove_sklad_name_sklad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
        migrations.AddField(
            model_name='sklad',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
