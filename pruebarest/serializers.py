from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostModelSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=20)
    body = serializers.CharField(max_length=100)
    slug = serializers.SlugField(required=False)

    def create(self, data):
        post = Post.objects.create(**data)
        return post
