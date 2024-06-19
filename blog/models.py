from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content= models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    views=models.PositiveIntegerField(default=0)
    likes= models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by{self.author} on {self.post}'
    
