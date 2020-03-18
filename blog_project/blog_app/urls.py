from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BlogPostViewSet, BlogCommentViewSet

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('blogpost', BlogPostViewSet, basename='blogpost')
router.register('blogcomment', BlogCommentViewSet, basename='blogComment')


urlpatterns = [
    path('', include(router.urls)),
]