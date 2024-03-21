from django.db import models


class Suppliers(models.Model):
    name_sup=models.CharField(max_length=150, verbose_name="Имя поставщика")
    name_kompani=models.CharField(max_length=150, verbose_name="Название компании")
    number_phone=models.CharField(max_length=15, verbose_name="Телефон")

    def __str__(self):
        return self.name_sup

class Categorii(models.Model):
    name_categorii=models.CharField(max_length=150, verbose_name="Название")

    def __str__(self):
        return self.name_categorii

class Product (models.Model):
    name_product=models.CharField(max_length=150, verbose_name="Название товара")

    suppliers=models.ForeignKey(Suppliers,verbose_name="Поставщик", on_delete=models.CASCADE,default=0)
    categorii=models.ForeignKey(Categorii,verbose_name="Категория", on_delete=models.CASCADE)



    price=models.DecimalField(max_digits=6, decimal_places=2 ,verbose_name="Цена")

    def __str__(self):
        return self.name_product

class Sklad (models.Model):

    product=models.ForeignKey(Product,verbose_name="Товар", on_delete=models.CASCADE)
    count=models.IntegerField( verbose_name="Количество",default=0)
    cell=models.CharField(max_length=10,verbose_name="Ячейка хранения")

    def __str__(self):
        return self.product.name_product







# Create your models here.
