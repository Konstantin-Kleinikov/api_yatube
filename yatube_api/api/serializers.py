"""Сериализаторы для приложения yatube_api."""
from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault()
    )
    group = serializers.SlugRelatedField(
        many=False,
        queryset=Group.objects.all(),
        slug_field='id',
        required=False,
        allow_null=True
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
