from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
import uuid
from django.contrib import auth


# Create your models here.
class Token(models.Model):
    '''маркер'''
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=255)


auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


class User(models.Model):
    '''пользователь'''
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True
