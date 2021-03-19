from rest_framework import serializers
from .models import Like, Post
from .models import Dislike
import json


class LikeAndDislikeSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField('like_counter')
    dislike_count = serializers.SerializerMethodField('dislike_counter')

    def dislike_counter(self, obj):
        dislikes = obj.dislike_set.all().count()
        return dislikes

    def like_counter(self, obj):
        likes = obj.like_set.all().count()
        return likes

    class Meta:
        model = Post
        fields = ('id', 'title', 'like_count', 'dislike_count')


# class DislikeSerializer(serializers.ModelSerializer):
#     dislike_count = serializers.SerializerMethodField('dislike_counter')
#
#     def dislike_counter(self, obj):
#         dislikes = obj.dislike_set.all().count()
#         return dislikes
#
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'dislike_count')