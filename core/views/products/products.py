from rest_framework.viewsets import ModelViewSet

from core.models.products.products import Product
from core.serializers.products.products import ProductSerializer, ProductListSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return ProductListSerializer
        return ProductSerializer