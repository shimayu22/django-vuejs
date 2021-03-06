from django.contrib.auth.models import User

from .models import PileColor, HedgeHog, Comment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  """ A serializer class for the User model """
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'username', 'password', 'is_active', 'is_superuser')

class PileColorSerializer(serializers.ModelSerializer):
  """ A serializer class for the PileColor model """
  class Meta:
    model = PileColor
    fields = ('id', 'name', 'description')

class HedgeHogSerializer(serializers.ModelSerializer):
  """ A serializer for the HedgeHog model """
  class Meta:
    model = HedgeHog
    fields = ('id', 'name', 'pile_color', 'starts', 'description', 'created')

class CommentSerializer(serializers.ModelSerializer):
  """ A serializer for the Comment model"""
  class Meta:
    model = Comment
    fields = ('id', 'user', 'hedgehog', 'comment', 'visible', 'created')

