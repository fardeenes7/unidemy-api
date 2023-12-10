from rest_framework.serializers import ModelSerializer
from .models import User
from django.conf import settings

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_superuser', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user