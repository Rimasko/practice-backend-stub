from rest_framework.serializers import ModelSerializer
from yandex_geocoder import Client
from apps.eats.models import Shop


yandexToken = '92697c91-37f6-41a4-84ae-a89645944328'


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        exclude = [ 'Owner']
        extra_kwargs = {
            'averge_cost': {'read_only': True},
            'lat': {'read_only': True},
            'lon': {'read_only': True},
        }

    def create(self, validated_data):
        owner = self.context['request'].user
        shop = Shop(**validated_data)
        shop.Owner = owner
        client = Client(yandexToken)
        shop.lat, shop.lon = client.coordinates(shop.addres)
        shop.save()
        return shop

