from rest_framework.viewsets import ModelViewSet
from core.models.orders.order_item_extra import OrderItemExtra
from core.serializers.orders.order_item_extra import OrderItemExtraSerializer, OrderItemExtraListSerializer

class OrderItemExtraViewSet(ModelViewSet):
    queryset = OrderItemExtra.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return OrderItemExtraListSerializer
        return OrderItemExtraSerializer