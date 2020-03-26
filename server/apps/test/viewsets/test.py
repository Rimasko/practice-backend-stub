from rest_framework.viewsets import mixins, GenericViewSet

from apps.test.models import Test
from apps.test.serializers import TestSerializer


class TestViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
