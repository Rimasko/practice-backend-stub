from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.filter(username=validated_data['username']).first()
        if user is None:
            user = User.objects.create_user(username=validated_data['username'],
                                            password=validated_data['password'])
        return user
