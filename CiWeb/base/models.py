#encoding=utf-8
from django.db import models

# Create your models here.


import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


@python_2_unicode_compatible
class NewUser(AbstractUser):
    profile = models.CharField('profile', default='',max_length=256)

    def __str__(self):
        return self.username