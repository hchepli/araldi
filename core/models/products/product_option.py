from django.db import models 

class ProductOption(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome', help_text='Nome da opção')
    additional_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Preço adicional', help_text='Preço adicional para esta opção')
    option_group = models.ForeignKey('ProductOptionGroup', on_delete=models.CASCADE, related_name='options', verbose_name='Grupo de opções', help_text='Grupo de opções ao qual esta opção pertence')
    active = models.BooleanField(default=True, verbose_name='Ativo', help_text='Indica se a opção está ativa')

    def __str__(self):
        return f"{self.name} - {self.option_group.name} - {self.option_group.product.name}"

    class Meta:
        verbose_name = 'Opção de Produto'
        verbose_name_plural = 'Opções de Produto'