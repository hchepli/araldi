from django.db import models


class OrderIntent(models.Model):

    class OriginChoices(models.TextChoices):
        SITE = "SITE", "Site"

    class DeliveryTypeChoices(models.TextChoices):
        DELIVERY = "DELIVERY", "Delivery"
        PICKUP = "PICKUP", "Retirada"

    class PaymentMethodChoices(models.TextChoices):
        PIX = "PIX", "Pix"
        CASH = "CASH", "Dinheiro"
        CARD = "CARD", "Cartão"

    class StatusChoices(models.TextChoices):
        GENERATED = "GENERATED", "Gerado"
        WHATSAPP_OPENED = "WHATSAPP_OPENED", "WhatsApp Aberto"

    # Identificação
    created_at = models.DateTimeField(auto_now_add=True)
    origin = models.CharField(
        max_length=20,
        choices=OriginChoices.choices,
        default=OriginChoices.SITE
    )

    # Dados do cliente
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20)

    # Entrega
    delivery_type = models.CharField(
        max_length=20,
        choices=DeliveryTypeChoices.choices
    )

    street = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    neighborhood = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    # Pagamento
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethodChoices.choices
    )
    change_for = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    # Valores
    subtotal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_fee_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Observações
    notes = models.TextField(blank=True, null=True)

    # Status
    status = models.CharField(
        max_length=30,
        choices=StatusChoices.choices,
        default=StatusChoices.GENERATED
    )

    def __str__(self):
        return f"Pedido #{self.id} - {self.customer_name}"

    class Meta:
        verbose_name = 'Intenção de Pedido'
        verbose_name_plural = 'Intenções de Pedidos'