from rest_framework.serializers import ModelSerializer
from core.models.promotions.promotion import Promotion

class PromotionSerializer(ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

class PromotionListSerializer(ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'date_start', 'date_end']