from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique = True,
        validators = [RegexValidator(
            regex = r'^@\w{3,}$',
            message = 'Username must consist of @ symbol followed by at least 3 alphanumericals'
            )]
    )
    first_name = models.CharField(
        max_length = 50, blank = False,
    )
    last_name = models.CharField(
        max_length = 50, blank = False,
    )
    email = models.EmailField(unique = True, blank = False)

    bio = models.CharField(max_length = 520, unique = False, blank = True)


class Post(models.Model):
    author = models.ForeignKey('User', on_delete = models.CASCADE)
    text = models.CharField(max_length = 280)
    created_at = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-created_at']
