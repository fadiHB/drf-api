from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .serializer import JokesSerializer
from .models import Jokes

from .permissions import PermissionsClass

# Create your views here.
class JokesListView(ListAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokesSerializer
    permissions_classes = (PermissionsClass,)

class JokesDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokesSerializer
    permissions_classes = (PermissionsClass,)
    