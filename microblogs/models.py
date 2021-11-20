from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from libgravatar import Gravatar


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

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def gravatar(self, size=120):
        """Return a URL to the user's gravatar."""
        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url

    def mini_gravatar(self):
        """Return a URL to a miniature version of the user's gravatar."""
        return self.gravatar(size=60)

    def toggle_follow(self, followee):
        """Toggles whether self follows the given followee."""

        pass

    def is_following(self, user):
        """Returns whether self follows the given user."""

        return False

    def follower_count(self):
        """Returns the number of followers of self."""

        return 0

    def followee_count(self):
        """Returns the number of followees of self."""

        return 0


class Post(models.Model):
    author = models.ForeignKey('User', on_delete = models.CASCADE)
    text = models.CharField(max_length = 280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
