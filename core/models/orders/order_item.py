from django.db import models
from .order_intent import OrderIntent


class OrderItem(models.Model):

    order_intent = models.ForeignKey(
        OrderIntent,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product_name = models.CharField(max_length=255)
    product_description = models.TextField(blank=True, null=True)

    quantity = models.PositiveIntegerField()

    base_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    additional_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_item_amount = models.DecimalField(max_digits=10, decimal_places=2)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.quantity}x {self.product_name}"

    class Meta:
        verbose_name = 'Item de Pedido'
        verbose_name_plural = 'Itens de Pedido'