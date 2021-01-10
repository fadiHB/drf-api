from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .serializer import JokesSerializer
from .models import Jokes

# Create your views here.
class JokesListView(ListAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokesSerializer

class JokesDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokesSerializer
    