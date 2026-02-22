from rest_framework.serializers import ModelSerializer

from core.models.users.user import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1
