from rest_framework import routers
from .api import CategoryViewSet, PresentationViewSet, PlasticViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, 'categories')
router.register('presentations', PresentationViewSet, 'presentations')
router.register('', PlasticViewSet, 'plastics')

urlpatterns = router.urls