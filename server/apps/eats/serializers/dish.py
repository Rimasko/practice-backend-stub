from rest_framework import serializers

from apps.eats.models import Dish, Ingridient


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"

    def create(self, validated_data):
        dish = Dish(name=validated_data['name'])
        dish.shop = validated_data['shop']
        dish.cost = validated_data['cost']
        dish.photo = validated_data['photo']
        dish.save()
        a = set()
        for i in validated_data['ingridients']:
            a.add(Ingridient.objects.get(pk=i.id))
        dish.ingridients.set(validated_data['ingridients'])
        dish.save()
        return dish
