from rest_framework import routers

from apps.test.viewsets import TestViewSet


router = routers.DefaultRouter()
router.register('test', TestViewSet, base_name='test')
