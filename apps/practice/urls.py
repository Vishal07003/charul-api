from rest_framework.routers import DefaultRouter
from .views import PracticeViewSet

router = DefaultRouter()

router.register(
    "",
    PracticeViewSet,
    basename="practice"
)

urlpatterns = router.urls