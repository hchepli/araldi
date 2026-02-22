from django.db import models

class ProductExtra(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome', help_text='Nome do extra do produto')
    product = models.OneToOneField('Product', on_delete=models.CASCADE, related_name='extra', verbose_name='Produto', help_text='Produto ao qual este extra pertence')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Preço', help_text='Preço do extra do produto')
    active = models.BooleanField(default=True, verbose_name='Ativo', help_text='Indica se o extra do produto está ativo')

    def __str__(self):
        return f"{self.name} - {self.product.name}"

    class Meta:
        verbose_name = 'Extra do Produto'
        verbose_name_plural = 'Extras dos Produtos'