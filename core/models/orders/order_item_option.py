from django.db import models
from .order_item import OrderItem


class OrderItemOption(models.Model):

    order_item = models.ForeignKey(
        OrderItem,
        on_delete=models.CASCADE,
        related_name="options"
    )

    option_group_name = models.CharField(max_length=255)
    option_name = models.CharField(max_length=255)
    additional_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.option_group_name}: {self.option_name}"

    class Meta:
        verbose_name = 'Opção do Item de Pedido'
        verbose_name_plural = 'Opções dos Itens de Pedido'