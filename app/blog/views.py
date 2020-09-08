from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class PostView(ModelViewSet):
    """List all the posts and post detail view. Create, update and delete the post"""

    queryset = Post.objects.all().annotate(count_votes=Count("votes"))
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentView(ModelViewSet):
    """List all the comments and single comment. Create, update and delete the comment"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpvoteAddView(APIView):
    """Add user's vote to the post"""

    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        if post.votes.filter(id=self.request.user.id).exists():
            post.votes.remove(self.request.user)
            return Response(status=201)
        post.votes.add(self.request.user)
        return Response(status=201)
