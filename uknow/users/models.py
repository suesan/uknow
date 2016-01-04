# --- coding: utf-8 ---
u"User Model"


import re
import uuid

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.core import validators
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        """ Creates and saves User with the given email and password. """
        now = timezone.now()
        token = str(uuid.uuid4())
        if not email:
            raise ValueError('Users must have an email address.')
        email = UserManager.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            token=token,
            is_active=True,
            last_login=now,
            date_joined=now,
            created_at=now,
            updated_at=now,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """ Creates and saves a superuser with the given email and password. """
        user = self.create_user(username, email, password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """User """
    username     = models.CharField(_('username'),
                                   max_length=30,
                                   unique=True,
                                   db_index=True,
                                   help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                                   '@/./+/-/_ characters'))
    first_name   = models.CharField(_('first name'), max_length=30, blank=True)
    last_name    = models.CharField(_('last name'), max_length=30, blank=True)
    email        = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    token        = models.CharField(_('token'), max_length=36, blank=True, unique=True, db_index=True)
    stock_count  = models.IntegerField(_('stock_count'), default=0, blank=False)
    contribution = models.IntegerField(_('contribution'), default=0, blank=False)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_admin     = models.BooleanField(default=False)
    date_joined  = models.DateTimeField(_('date joined'), default=timezone.now)
    created_at   = models.DateTimeField(_('created_at'), auto_now_add=True, blank=True)
    updated_at   = models.DateTimeField(_('updated_at'), default=timezone.now)
    delete       = models.BooleanField(default=0)


    objects = UserManager()

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    def email_user(self, subject, message, from_email=None):
        """Send an email to this User. """
        send_mail(subject, message, from_email, [self.email])

    def user_has_perm(user, perm, obj):
        """
        A backend can raise `PermissionDenied` to short-circuit permission checking.
        """
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin
