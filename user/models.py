from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class TweetaUser(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    location = models.CharField(max_length=100)
    user = models.OneToOneField(TweetaUser, on_delete=models.CASCADE, primary_key=True)
