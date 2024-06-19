from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, CommentViewSet, UserViewSet,home

router=DefaultRouter()
router.register('posts', BlogPostViewSet)
router.register('comments', CommentViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('',home,name='home'),
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]