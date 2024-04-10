from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Categorii, Product, Sklad, Suppliers
from django.contrib.auth.models import User
from .serializers import ProductSerializer, SkladSerializer

class AptekaTests(APITestCase):
    def setUp(self) -> None:
       self.categiorii = Categorii.objects.create(name_categorii = "categorii")
       self.suppliers = Suppliers.objects.create(name_sup = "Suppliers_test",name_kompani ="kompani_test", number_phone ="89243837255")
       self.product = Product.objects.create(name_product="product_test", suppliers = self.suppliers,categorii = self.categiorii,price="100")
       self.user=User.objects.create_user("test","test@test.ru")
       self.skad = Sklad.objects.create(product=self.product,count=100,cell="A212")

    def test_anonymous_user_sklad(self):
        response = self.client.get("/api/Sklad/",format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_anonymous_user_product(self):
        response = self.client.get("/api/Product/",format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_sklad(self):
        self.client.force_login(self.user)
        response = self.client.get("/api/Sklad/",format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
        serializer = SkladSerializer(Sklad.objects.all(),many=True)
        self.assertListEqual(response.data,serializer.data)

    def test_get_product_id(self):
        self.client.force_login(self.user)
        response = self.client.get(f'/api/product/{self.product.id}/',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        serializer = ProductSerializer(Product.objects.get(id=self.product.id))
        self.assertDictEqual(response.data,serializer.data)

    def test_post_product(self):
        self.client.force_login(self.user)
        response = self.client.post('/api/Product/',{'name_product' : "test","suppliers" : 1, 'categorii':1,"price": 100},format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
