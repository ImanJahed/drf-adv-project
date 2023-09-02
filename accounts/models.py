from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, verbose_name=_('username'))
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin