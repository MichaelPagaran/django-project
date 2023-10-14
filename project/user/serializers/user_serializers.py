from rest_framework.serializers import ModelSerializer, ModelField
from models.user import User

class UserSummarySerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'birthdate')

class UserDetailSerializer(ModelField):
    class Meta:
        model = User
        fields = '__all__'