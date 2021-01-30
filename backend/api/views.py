from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer, StoreSerializer
from .models import User, Store

# Create your views here.
class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
