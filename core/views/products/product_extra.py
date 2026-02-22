from rest_framework.viewsets import ModelViewSet

from core.models.products.product_extra import ProductExtra
from core.serializers.products.product_extra import ProductExtraSerializer, ProductExtraListSerializer

class ProductExtraViewSet(ModelViewSet):
    queryset = ProductExtra.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return ProductExtraListSerializer
        return ProductExtraSerializer