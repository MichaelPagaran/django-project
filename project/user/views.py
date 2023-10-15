from django.shortcuts import render
from rest_framework import viewsets

from .models.user import User
from .models.account import Account

from .serializers.user_serializers import UserDetailSerializer, UserSummarySerializer
from .serializers.account_serializer import AccountDetailSerializer

class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class AccountDetailViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer
