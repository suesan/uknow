from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from users.models import User


class Poem(models.Model):
    """docstring for """
    poem        = models.CharField(_('poem'), max_length=255)
    created_at  = models.DateTimeField(_('created_at'), auto_now_add=True, blank=True)
    updated_at  = models.DateTimeField(_('updated_at'), default=timezone.now)
    delete      = models.BooleanField(default=0)

class Tag(models.Model):
    """docstring for """
    count       = models.IntegerField(_('count'), default=0, blank=False)
    created_at  = models.DateTimeField(_('created_at'), auto_now_add=True, blank=True)
    updated_at  = models.DateTimeField(_('updated_at'), default=timezone.now)
    delete      = models.BooleanField(default=0)

class Stock(models.Model):
    """docstring for """
    poem        = models.ForeignKey(Poem)
    user        = models.ForeignKey(User)
    created_at  = models.DateTimeField(_('created_at'), auto_now_add=True, blank=True)
    updated_at  = models.DateTimeField(_('updated_at'), default=timezone.now)
    delete      = models.BooleanField(default=0)
