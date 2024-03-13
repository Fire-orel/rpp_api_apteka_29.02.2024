from rest_framework import serializers

from .models import Sklad,Product,Suppliers,Categorii

class CategoriiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categorii
        fields=("id","name_categorii")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=("id","name_product","suppliers","categorii","count","price")


class SkladSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sklad
        fields=("id","product","cell")

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Suppliers
        fields=("id","name_sup","name_kompani","number_phone")
