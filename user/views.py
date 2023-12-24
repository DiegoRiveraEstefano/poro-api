from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer


class UserRegister(generics.CreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):

        data = request.data
        print(data)

        expected_data = ['username', 'password', 'email']
        if expected_data != list(data.keys()):
            return Response(status=404)

        if len(User.objects.filter(username=data["username"])) != 0:
            return Response(status=401)

        user = User.objects._create_user(username=data['username'], password=data['password'], email=data['email'])
        user.save()
        return Response(200)






