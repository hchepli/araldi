from rest_framework.viewsets import ModelViewSet

from core.models.products.product_option_group import ProductOptionGroup
from core.serializers.products.product_option_group import ProductOptionGroupSerializer, ProductOptionGroupListSerializer

class ProductOptionGroupViewSet(ModelViewSet):
    queryset = ProductOptionGroup.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return ProductOptionGroupListSerializer
        return ProductOptionGroupSerializer