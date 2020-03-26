from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.eats.models import Ingridient
from apps.eats.serializers import IngridientSerializer


class IngridientViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    serializer_class = IngridientSerializer
    queryset = Ingridient.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)
