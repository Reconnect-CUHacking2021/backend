from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from django.views.generic import View
from rest_framework.permissions import IsAuthenticated
import qrcode
import qrcode.image.svg
from io import BytesIO

from .serializers import UserSerializer, StoreSerializer, CodeSerializer
from .models import User, Store, Code

# pylint: disable=no-member
# Create your views here.
class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=True)
    def retrieve_code(self, request):
        print(request.User)
        return JsonResponse({
            "hello": "hi"
        })

    @action(methods=['POST'], detail=True)
    def favourite(self, request):
        return JsonResponse({
            "hello": "bruh"
        })


class CodeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    # permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=True)
    def enter(self, request, pk=None):
        return JsonResponse({
            "hello": "hi"
        })

    @action(methods=['GET'], detail=True)
    def generate(self, request, pk=None):
        print("wasd", pk)
        byte_io = BytesIO()
        qrImg = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qrImg.add_data(pk)
        qrImg.make(fit=True)

        img = qrImg.make_image(fill_color="black", back_color="white")
        print(type(img))
        img.save(byte_io, 'PNG')
        # return JsonResponse({
        #     "hello": "ok generating bs"
        # })
        return HttpResponse(byte_io.getvalue(), content_type="image/jpeg")

