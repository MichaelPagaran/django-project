from rest_framework.serializers import ModelSerializer, ModelField
from user.models.user import User

class UserSummarySerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'birthdate')

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'