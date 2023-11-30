from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'images', ImageViewSet, basename='image')

