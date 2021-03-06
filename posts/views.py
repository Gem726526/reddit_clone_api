from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster = self.request.user)
        
class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter= user, post=post)

    def perform_create(self, serializer):
        print("Hello")
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this Post')
        serializer.save (voter = self.request.user , post = Post.objects.get(pk=self.kwargs['pk']))

