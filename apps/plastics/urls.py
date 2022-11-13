from rest_framework import routers
from .api import CategoryViewSet, PresentationViewSet, PlasticViewSet

router = routers.DefaultRouter()

router.register('api/categories', CategoryViewSet, 'categories')
router.register('api/presentations', PresentationViewSet, 'presentations')
router.register('api/plastics', PlasticViewSet, 'plastics')

urlpatterns = router.urls