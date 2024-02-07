from django.db import models

from tweet.models import Tweet


# Create your models here.


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    commented_on = models.DateTimeField(auto_now=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweet_comment')

    def __str__(self):
        return self.comment


class Meta:
    ordering = ['last_update']
