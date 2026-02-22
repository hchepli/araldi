from django.db import models

class ProductOptionGroup(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nome', help_text='Nome do grupo de opções')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição', help_text='Descrição do grupo de opções')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='option_groups', verbose_name='Produto', help_text='Produto ao qual este grupo de opções pertence')
    mandatory = models.BooleanField(default=False, verbose_name='Obrigatório', help_text='Indica se a seleção de uma opção deste grupo é obrigatória')
    multiple_choice = models.BooleanField(default=False, verbose_name='Múltipla escolha', help_text='Indica se é permitido selecionar múltiplas opções deste grupo')

    def  __str__(self):
        return f"{self.name} - {self.product.name}"

    class Meta:
        verbose_name = 'Grupo de Opções'
        verbose_name_plural = 'Grupos de Opções'