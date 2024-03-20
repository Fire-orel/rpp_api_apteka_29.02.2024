from rest_framework.viewsets import ModelViewSet
from .models import Categorii,Product,Sklad,Suppliers
from .serializers import ProductSerializer,CategoriiSerializer,SkladSerializer,SuppliersSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ('get', 'post', 'put')
    @action(methods=['GET'], detail=False)
    def productcounts(self, request):
        print(request.user)
        qs=self.get_queryset().filter(count__gte=75)
        serializer=self.get_serializer_class()(qs,many=True)
        return Response(data=serializer.data)


class CategoriiViewSet(ModelViewSet):
    queryset = Categorii.objects.all()
    serializer_class = CategoriiSerializer
    http_method_names = ('get', 'post', 'put')

class SkladViewSet(ModelViewSet):
    queryset = Sklad.objects.all()
    serializer_class = SkladSerializer
    http_method_names = ('get', 'post', 'put')

class SuppliersViewSet(ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    http_method_names = ('get', 'post', 'put')
# Create your views here.
