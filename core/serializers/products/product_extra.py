from rest_framework.serializers import ModelSerializer
from core.models.products.product_extra import ProductExtra

class ProductExtraSerializer(ModelSerializer):
    class Meta:
        model = ProductExtra
        fields = '__all__'

class ProductExtraListSerializer(ModelSerializer):
    class Meta:
        model = ProductExtra
        fields = ['id', 'product', 'name', 'price', 'active']