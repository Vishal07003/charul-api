from rest_framework.routers import DefaultRouter
from .views import StatViewSet


router = DefaultRouter()

router.register(
    "",
    StatViewSet,
    basename="stats"
)

urlpatterns = router.urls