from rest_framework.serializers import ModelSerializer
from core.models.orders.order_intent import OrderIntent

class OrderIntentSerializer(ModelSerializer):
    class Meta:
        model = OrderIntent
        fields = '__all__'

class OrderIntentListSerializer(ModelSerializer):
    class Meta:
        model = OrderIntent
        fields = ['id', 'status', 'total_amount', 'origin', 'customer_name']