from rest_framework.serializers import ModelSerializer
from core.models.products.product_option import ProductOption

class ProductOptionSerializer(ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'

class ProductOptionListSerializer(ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['id', 'option_group', 'name', 'active', 'additional_price']