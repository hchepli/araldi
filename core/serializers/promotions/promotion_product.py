from rest_framework.serializers import ModelSerializer
from core.models.promotions.promotion_product import PromotionProduct

class PromotionProductSerializer(ModelSerializer):
    class Meta:
        model = PromotionProduct
        fields = '__all__'

class PromotionProductListSerializer(ModelSerializer):
    class Meta:
        model = PromotionProduct
        fields = ['id', 'promotion', 'product', 'discount_percentage']