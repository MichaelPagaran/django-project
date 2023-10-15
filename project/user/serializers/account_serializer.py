from rest_framework.serializers import ModelSerializer, ModelField
from user.models.account import Account

class AccountDetailSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

