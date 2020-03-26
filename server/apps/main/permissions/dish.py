from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.eats.models import Shop


class DishPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated and 'shop' in request.data:
            owner = request.user
            print(owner)
            try:
                shop = Shop.objects.get(pk=request.data['shop'])
                if shop.Owner == owner:
                    return True
            except Shop.DoesNotExist:
                return False

        return False
