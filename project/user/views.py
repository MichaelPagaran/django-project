from django.shortcuts import render
from rest_framework import viewsets

from models.user import User

from serializers.user_serializers import UserDetailSerializer, UserSummarySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    