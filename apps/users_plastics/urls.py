from rest_framework import routers
from .viewsets import OriginViewSet, User_PlasticViewSet

router = routers.DefaultRouter()

router.register('origins', OriginViewSet, 'origenes')
router.register('', User_PlasticViewSet, 'users_plastics')

urlpatterns = router.urls