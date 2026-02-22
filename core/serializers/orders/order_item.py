from rest_framework.serializers import ModelSerializer
from core.models.orders.order_item import OrderItem

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderItemListSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order_intent', 'product_name', 'quantity', 'unit_price', 'total_price']