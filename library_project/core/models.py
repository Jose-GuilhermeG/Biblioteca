#imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

USER = get_user_model()

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(
        _("Criado em"),
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        _("Atualizado em"),
        auto_now=True
    )
    
    class Meta:
        abstract=True
        ordering = ['-created_at']
        
        
class CanBeMonitorated(
    BaseModel
):
    created_by = models.ForeignKey(
        verbose_name=_("Criado por"),
        to=USER,
        on_delete=models.SET_NULL,
        related_name="creations",
        null=True
    )
    
    updated_by = models.ForeignKey(
        verbose_name=_("Atualizado por"),
        to=USER,
        on_delete=models.SET_NULL,
        related_name="updateds",
        null=True
    )
    
    class Meta:
        abstract = True