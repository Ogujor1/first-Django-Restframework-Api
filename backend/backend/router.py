from rest_framework.routers import DefaultRouter
from product.viewset import ProductViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename='products')

urlpatterns = router.urls

