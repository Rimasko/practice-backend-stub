from rest_framework import routers

from apps.test.viewsets import TestViewSet
from apps.users.viewsets import UserViewSet
from apps.eats.viewsets import ShopViewSet
from apps.eats.viewsets import IngridientViewSet
from apps.eats.viewsets import DishViewSet

router = routers.DefaultRouter()
router.register('test', TestViewSet, base_name='test')
router.register('users', UserViewSet, base_name='user')
router.register('shop', ShopViewSet, base_name='shop')
router.register('dish', DishViewSet, base_name='dish')
router.register('ingridient', IngridientViewSet, base_name='ingridient')
