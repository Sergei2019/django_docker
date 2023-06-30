from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(_('Имя'), max_length=150)
    last_name = models.CharField(_("Фамилия"), max_length=150)
    email = models.EmailField(_("E-mail"), max_length=250, unique=True)
    username = models.CharField(_("Username"), max_length=250, unique=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("email", "first_name", "last_name")
