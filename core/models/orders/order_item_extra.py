from django.db import models
from .order_item import OrderItem


class OrderItemExtra(models.Model):

    order_item = models.ForeignKey(
        OrderItem,
        on_delete=models.CASCADE,
        related_name="extras"
    )

    extra_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.extra_name} ({self.quantity}x)"

    class Meta:
        verbose_name = 'Extra do Item de Pedido'
        verbose_name_plural = 'Extras dos Itens de Pedido'