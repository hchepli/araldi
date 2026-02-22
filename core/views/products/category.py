from rest_framework.viewsets import ModelViewSet

from core.models.products.category import Category
from core.serializers.products.category import CategorySerializer, CategoryListSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return CategoryListSerializer
        return CategorySerializer