from rest_framework.viewsets import ModelViewSet

from core.models.promotions.promotion_product import PromotionProduct
from core.serializers.promotions.promotion_product import PromotionProductSerializer, PromotionProductListSerializer

class PromotionProductViewSet(ModelViewSet):
    queryset = PromotionProduct.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return PromotionProductListSerializer
        return PromotionProductSerializer