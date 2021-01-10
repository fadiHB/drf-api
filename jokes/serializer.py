from rest_framework import serializers

from .models import Jokes

class JokesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body')
        model = Jokes
