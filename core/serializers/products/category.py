from rest_framework.serializers import ModelSerializer
from core.models.products.category import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'active']