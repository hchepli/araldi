from rest_framework.viewsets import ModelViewSet

from core.models.promotions.promotion import Promotion
from core.serializers.promotions.promotion import PromotionSerializer, PromotionListSerializer

class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return PromotionListSerializer
        return PromotionSerializer