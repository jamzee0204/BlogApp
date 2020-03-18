from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    blogger = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogCommentSerializer(serializers.ModelSerializer):
    blog_post = serializers.PrimaryKeyRelatedField(queryset=BlogPost.objects.all())

    class Meta:
        model = BlogComment
        fields = '__all__'