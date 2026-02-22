from rest_framework.serializers import ModelSerializer
from core.models.products.products import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'active', 'category', 'highlight']