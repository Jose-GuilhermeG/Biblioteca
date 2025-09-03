#imports
from django.db import models
from core.models import CanBeMonitorated
from core.constans import MEDIUN_CHAR_SIZE
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

USER = get_user_model()

# Create your models here.
class Book(
    CanBeMonitorated
):
    
    author = models.ForeignKey(
        verbose_name=_("Autor do livro"),
        to=USER,
        related_name='books',
        on_delete=models.PROTECT,
        blank=True
    )
    
    title = models.CharField(
        verbose_name=_("Titulo do livro"),
        max_length=MEDIUN_CHAR_SIZE,
        unique=True,
        blank=False,
        null=False,
    )
    
    slug = models.SlugField(
        _("Slug do livro"),
        unique=True,
        null=True,
    )
    
    desciption = models.TextField(
        verbose_name=_("Descrição do livro"),
        blank=True,
        null=False,
        help_text=_("Descrição do livro, sem tamanho maximo aceita qualquer caracter e pode estar vazia")
    )
    
    price = models.DecimalField(
        verbose_name=_("Preço do livro"),
        decimal_places=2,
        max_digits=5,
        null=True,
        default=0,
    )
    
    content = models.TextField(
        verbose_name=_("Conteudo do livro"),
        blank=True,
        null=True,
    )
    
    file = models.FileField(
        verbose_name=_("Arquivo do livro"),
        upload_to='book/files/',
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.title
    
    def is_free(self):
        return self.price == 0
    
    class Meta:
        verbose_name =_("Livro")
        verbose_name_plural =_("Livros")