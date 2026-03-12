from django.contrib import admin
from django.urls import path, include
from posts.views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# router = routers.SimpleRouter()
# router.register(r'post', PostsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/post/', PostsAPIList.as_view()),
    path('api/v1/post/<int:pk>/', PostsAPIUpdate.as_view()),
    path('api/v1/postdelete/<int:pk>/', PostsAPIDestroy.as_view()),
    path('api/v1/postcomment/', CommentAPIList.as_view()),
    path('api/v1/postcomment/<int:pk>/', CommentAPIDestroy.as_view()),
    
    # path('api/v1/postlist/', PostsViewSet.as_view({'get': 'list'})),
    # path('api/v1/postlist/<int:pk>/', PostsViewSet.as_view({'put': 'update'}))  
]
