from django.urls import path,include

from rest_framework import routers
from .views import CategoriiViewSet,ProductViewSet,SuppliersViewSet,SkladViewSet

router=routers.DefaultRouter()
router.register('Product', ProductViewSet),
router.register("Categorii",CategoriiViewSet)
router.register("Suppliers",SuppliersViewSet)
router.register("Skad",SkladViewSet)

urlpatterns = [
    path("api/",include(router.urls)),
]
