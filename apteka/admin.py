from django.contrib import admin
from .models import Categorii, Product,Suppliers,Sklad

admin.site.register(Suppliers)
admin.site.register(Categorii)
admin.site.register(Product)
admin.site.register(Sklad)

# Register your models here.
