# Generated by Django 5.0.2 on 2024-03-21 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apteka', '0004_sklad_name_sklad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sklad',
            name='name_sklad',
        ),
    ]