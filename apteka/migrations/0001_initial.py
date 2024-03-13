# Generated by Django 5.0.2 on 2024-02-29 02:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_categorii', models.CharField(max_length=150, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_sup', models.CharField(max_length=150, verbose_name='Имя поставщика')),
                ('name_kompani', models.CharField(max_length=150, verbose_name='Название компании')),
                ('number_phone', models.CharField(max_length=15, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=150, verbose_name='Название товара')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('categorii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka.categorii', verbose_name='Категория')),
            ],
        ),
    ]