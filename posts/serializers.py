from django.db.models import fields
from rest_framework import serializers
from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    #poster = serializers.ReadOnlyField(source = 'poster.username') 
    poster_username = serializers.ReadOnlyField(source = 'poster.username')
    
    class Meta:
        model = Post
        fields =['id', 'title', 'url', 'poster', 'poster_username', 'created_on', ]
        read_only_fields = ['poster', ]

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields  = ['id']

