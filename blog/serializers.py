from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import BlogPost, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class BlogPostSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    
    class Meta:
        model=BlogPost
        fields=['id','title','content','author','views','likes','created_at']

class CommentSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    post=serializers.PrimaryKeyRelatedField(queryset=BlogPost.objects.all())
    
    class Meta:
        model=Comment
        fields=['id','post','author','content','created_at']