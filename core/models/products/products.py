from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nome', help_text='Nome do produto')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição', help_text='Descrição do produto')
    #image = models.URLField(blank=True, null=True, verbose_name='Imagem', help_text='URL da imagem do produto')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço', help_text='Preço do produto')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', verbose_name='Categoria', help_text='Categoria do produto')
    active = models.BooleanField(default=True, verbose_name='Ativo', help_text='Indica se o produto está ativo')
    highlight = models.BooleanField(default=False, verbose_name='Destaque', help_text='Indica se o produto é destaque')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'