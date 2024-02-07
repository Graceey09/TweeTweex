from rest_framework import serializers

from comment.models import Comment
from tweet.models import Tweet


class TweetSerializer(serializers.Serializer):
    last_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Tweet
        fields = ("text", "last_update", "user")


class CommentSerializer(serializers.Serializer):
    commented_on = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ("comment", "commented_on", "tweet")
