from django.db import models

class Promotion(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nome', help_text='Nome da promoção')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição', help_text='Descrição da promoção')
    date_start = models.DateTimeField(verbose_name='Data de início', help_text='Data e hora de início da promoção')
    date_end = models.DateTimeField(verbose_name='Data de término', help_text='Data e hora de término da promoção')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Promoção'
        verbose_name_plural = 'Promoções'