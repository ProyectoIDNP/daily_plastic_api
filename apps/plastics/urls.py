from rest_framework import routers
from .viewsets import CategoryViewSet, PresentationViewSet, PlasticViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, 'categories')
router.register('presentations', PresentationViewSet, 'presentations')
router.register('', PlasticViewSet, 'plastics')

urlpatterns = router.urls