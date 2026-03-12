from rest_framework import serializers 
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = '__all__'
        
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = '__all__'
    
    
