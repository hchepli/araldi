from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nome', help_text='Nome da categoria')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição', help_text='Descrição da categoria')
    display_order = models.PositiveIntegerField(default=0, verbose_name='Ordem de exibição', help_text='Ordem de exibição da categoria')
    active = models.BooleanField(default=True, verbose_name='Ativo', help_text='Indica se a categoria está ativa')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'