from rest_framework.viewsets import ModelViewSet

from core.models.products.product_option import ProductOption
from core.serializers.products.product_option import ProductOptionSerializer, ProductOptionListSerializer

class ProductOptionViewSet(ModelViewSet):
    queryset = ProductOption.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return ProductOptionListSerializer
        return ProductOptionSerializer