from rest_framework.viewsets import ModelViewSet
from core.models.orders.order_intent import OrderIntent
from core.serializers.orders.order_intent import OrderIntentSerializer, OrderIntentListSerializer

class OrderIntentViewSet(ModelViewSet):
    queryset = OrderIntent.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return OrderIntentListSerializer
        return OrderIntentSerializer