from django.db import models
from core.models.products.products import Product
from core.models.promotions.promotion import Promotion

class PromotionProduct(models.Model):
    promotion = models.ForeignKey(
        Promotion,
        on_delete=models.CASCADE,
        related_name='promotion_products'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_promotions'
    )
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Desconto (%)',
        help_text='Porcentagem de desconto aplicada ao produto nesta promoção'
    )

    def __str__(self):
        return f"{self.promotion.name} - {self.product.name}"

    class Meta:
        verbose_name = 'Produto da Promoção'
        verbose_name_plural = 'Produtos das Promoções'