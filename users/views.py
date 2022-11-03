import ipdb
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics

from drf_spectacular.utils import extend_schema
from psytube.pagination import CustomPageNumberPagination


from users.models import User
from users.serializers import SoftDeleteSerializer, UserRetriveUpdateSerializer, UserSerializer


class AccountsViews(generics.CreateAPIView):
    queryset = User.objects.all()
    get_serializer = UserSerializer


@extend_schema(methods=["PUT"], exclude=True)
class AccountsDetailsViews(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserRetriveUpdateSerializer

    pagination_class = CustomPageNumberPagination

    def get_object(self):
        return self.request.user


class ListAccountViews(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserRetriveUpdateSerializer

    pagination_class = CustomPageNumberPagination


@extend_schema(methods=["PUT"], exclude=True)
class SoftDeleteViews(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = SoftDeleteSerializer

    pagination_class = CustomPageNumberPagination


class UsersViews(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    pagination_class = CustomPageNumberPagination
