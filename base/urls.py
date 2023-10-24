from django.urls import path
from .views import ProductListViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"api/shop", ProductListViewSet)

urlpatterns = [
] + router.urls
