from api.views import UserViewSet, StoreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'store', StoreViewSet, basename='store')

urlpatterns = router.urls
