from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import *
from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


# class PostsViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostsAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    
class PostsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    
       
class PostsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    
class CommentAPIList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    
class CommentAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminOrReadOnly,)

