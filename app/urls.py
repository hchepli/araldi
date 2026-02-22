from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views.users.user import UserViewSet
from core.views.products.products import ProductViewSet
from core.views.products.product_option_group import ProductOptionGroupViewSet
from core.views.products.product_option import ProductOptionViewSet
from core.views.products.product_extra import ProductExtraViewSet
from core.views.products.category import CategoryViewSet
from core.views.orders.order_intent import OrderIntentViewSet
from core.views.orders.order_item import OrderItemViewSet
from core.views.orders.order_item_option import OrderItemOptionViewSet
from core.views.orders.order_item_extra import OrderItemExtraViewSet
from core.views.promotions.promotion import PromotionViewSet
from core.views.promotions.promotion_product import PromotionProductViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'product-option-groups', ProductOptionGroupViewSet, basename='product-option-groups')
router.register(r'product-options', ProductOptionViewSet, basename='product-options')
router.register(r'product-extras', ProductExtraViewSet, basename='product-extras')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'order-intents', OrderIntentViewSet, basename='order-intents')
router.register(r'order-items', OrderItemViewSet, basename='order-items')
router.register(r'order-item-options', OrderItemOptionViewSet, basename='order-item-options')
router.register(r'order-item-extras', OrderItemExtraViewSet, basename='order-item-extras')
router.register(r'promotions', PromotionViewSet, basename='promotions')
router.register(r'promotion-products', PromotionProductViewSet, basename='promotion-products')
urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
