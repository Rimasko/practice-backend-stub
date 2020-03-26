from django.contrib.auth.models import User

from rest_framework import viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from apps.users.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,
                             'username': user.username,
                             'password': user.password},
                            status=HTTP_201_CREATED)
        else:
            return Response({'Erorr': 'NO valid data'}, status=404)