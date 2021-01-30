from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from django.views.generic import View

from .serializers import UserSerializer, StoreSerializer, CodeSerializer
from .models import User, Store, Code

# pylint: disable=no-member
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    @action(methods=['post'], detail=True)
    def retrieve_code(self, request):
        return JsonResponse({
            "hello": "hi"
        })


class CodeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

    @action(methods=['post'], detail=True)
    def enter(self, request, pk=None):
        return JsonResponse({
            "hello": "hi"
        })

