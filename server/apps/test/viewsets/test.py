from rest_framework.viewsets import ModelViewSet

from apps.test.models import Test
from apps.test.serializers import TestSerializer


class TestViewSet(ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
