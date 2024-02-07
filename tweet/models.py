from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=200)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['last_update']


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    commented_on = models.DateTimeField(auto_now=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweet_comment')
