from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.eats.models import Dish
from apps.eats.serializers import DishSerializer
from apps.main.permissions import DishPermission


class DishViewSet(ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    permission_classes = [DishPermission]

