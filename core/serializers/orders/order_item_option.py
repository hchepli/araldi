from rest_framework.serializers import ModelSerializer
from core.models.orders.order_item_option import OrderItemOption

class OrderItemOptionSerializer(ModelSerializer):
    class Meta:
        model = OrderItemOption
        fields = '__all__'

class OrderItemOptionListSerializer(ModelSerializer):
    class Meta:
        model = OrderItemOption
        fields = ['id', 'order_item', 'option_group_name', 'option_name', 'additional_price']