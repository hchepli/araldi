from rest_framework.serializers import ModelSerializer
from core.models.products.product_option_group import ProductOptionGroup

class ProductOptionGroupSerializer(ModelSerializer):
    class Meta:
        model = ProductOptionGroup
        fields = '__all__'

class ProductOptionGroupListSerializer(ModelSerializer):
    class Meta:
        model = ProductOptionGroup
        fields = ['id', 'product', 'name']