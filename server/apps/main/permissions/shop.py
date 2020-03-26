from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.eats.models import Shop


class ShopPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated:
            if request.method == "POST":
                return True
            if 'pk' not in view.kwargs or 'id' not in request.data:
                return False
            if view.kwargs['pk'] != request.data['id']:
                return False
            owner = request.user
            try:
                shop = Shop.objects.get(pk=request.data['id'])
                if shop.Owner == owner:
                    return True
            except Shop.DoesNotExist:
                return False
        return False
