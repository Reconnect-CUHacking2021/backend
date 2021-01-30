from api.views import (
    UserViewSet, 
    StoreViewSet, 
    CodeViewSet,     
)
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'store', StoreViewSet, basename='store')
router.register(r'code', CodeViewSet, basename='code')

urlpatterns = router.urls