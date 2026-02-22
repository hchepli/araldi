from rest_framework.serializers import ModelSerializer
from core.models.orders.order_item_extra import OrderItemExtra

class OrderItemExtraSerializer(ModelSerializer):
    class Meta:
        model = OrderItemExtra
        fields = '__all__'

class OrderItemExtraListSerializer(ModelSerializer):
    class Meta:
        model = OrderItemExtra
        fields = ['id', 'order_item', 'extra_name', 'total_price', 'quantity']