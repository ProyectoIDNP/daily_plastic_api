from rest_framework import routers
from .api import OriginViewSet, User_PlasticViewSet

router = routers.DefaultRouter()

router.register('api/origins', OriginViewSet, 'origenes')
router.register('api/users/plastics', User_PlasticViewSet, 'users_plastics')

urlpatterns = router.urls