from rest_framework.viewsets import ModelViewSet
from core.models.orders.order_item import OrderItem
from core.serializers.orders.order_item import OrderItemSerializer, OrderItemListSerializer

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return OrderItemListSerializer
        return OrderItemSerializer