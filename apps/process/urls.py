from rest_framework.routers import DefaultRouter
from .views import ProcessViewSet

router = DefaultRouter()

router.register( "", ProcessViewSet, basename="process")

urlpatterns = router.urls