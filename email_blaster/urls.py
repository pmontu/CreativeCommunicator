from rest_framework.routers import SimpleRouter
from .views import MessageViewSet

router = SimpleRouter()
router.register(r"messages", MessageViewSet, basename='messages')

urlpatterns = router.urls
