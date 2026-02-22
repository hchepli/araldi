from rest_framework.viewsets import ModelViewSet
from core.models.orders.order_item_option import OrderItemOption
from core.serializers.orders.order_item_option import OrderItemOptionSerializer, OrderItemOptionListSerializer

class OrderItemOptionViewSet(ModelViewSet):
    queryset = OrderItemOption.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return OrderItemOptionListSerializer
        return OrderItemOptionSerializer