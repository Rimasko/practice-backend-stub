from rest_framework import serializers

from apps.eats.models import Ingridient


class IngridientSerializer(serializers.ModelSerializer):
    dishes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ingridient
        fields = "__all__"
