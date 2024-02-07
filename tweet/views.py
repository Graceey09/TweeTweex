from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

import comment

# RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView

import tweet
from tweet.models import Tweet, Comment
from tweet.serializers import TweetSerializer, CommentSerializer


# Create your views here.

class TweetList(APIView):
    def get(self):
        tweet = Tweet.objects.all()
        serializer = TweetSerializer(tweet, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TweetDetail(RetrieveDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def perform_destroy(self, tweet):
        if tweet.user == self.request.user:
            tweet.delete


class CommentList(ListCreateAPIView):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# @api_view(['GET', 'POST'])
# def tweet_list_and_create(request):
#     if request.GET == "GET":
#         tweets = Tweet.objects.all()  # SELECT * FROM Tweets  -- return list
#         # one_tweet = Tweet.objects.get(pk=17)  # SELECT * FROM Tweets WHERE pk IS 17 -- return {}
#         tweet_serializer = TweetSerializer(tweets, many=True)
#         return Response(tweet_serializer.data, status=status.HTTP_200_OK)
#     elif request.POST == "POST":
#         data = request.body
# Tweet.objects.create(
#     text=data.get("text")
# )
#
#         serializer = TweetSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def tweet_detail(request, pk):
#     tweet = get_object_or_404(Tweet, pk=pk)
#
#     if request.method == 'GET':
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = TweetSerializer(tweet, data=request.data)
