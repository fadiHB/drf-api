from django.contrib import admin
from django.urls import path, include


from .views import JokesDetailsView, JokesListView


urlpatterns = [
    path('', JokesListView.as_view(), name='jokes'),
    path('<int:pk>/', JokesDetailsView.as_view(), name='jokes_details'),
]
