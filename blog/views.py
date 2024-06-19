from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from blog.models import BlogPost, Comment
from .serializers import UserSerializer, BlogPostSerializer, CommentSerializer
from django.db.models import Count,F
from django.http import HttpResponse

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    @action(detail=False, methods=['get'],permission_classes=[permissions.AllowAny])
    def trending(self, request):
        trending_posts=BlogPost.objects.annotate(
            popularity=F('views')+F('likes')+Count('comments')
        ).order_by('-popularity')
        serializer=self.get_serializer(trending_posts, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

def home(request):
    return HttpResponse('Welcome to the blog, please visit /api/ to view the API endpoints.')

