from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, LeadViewSet

router = DefaultRouter()
router.register(
    "leads",
    LeadViewSet,
    basename="lead"
)
router.register(
    "",
    ContactViewSet,
    basename="contact"
)
urlpatterns = router.urls