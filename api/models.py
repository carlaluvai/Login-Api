from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

# def upload_location(instance, filename, **kwargs):
#     file_path = 'login/{username}/-{filename}'.format(
#         username=str(instance.username), filename=filename
#     )
#     return file_path


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    location = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10)
    # image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


