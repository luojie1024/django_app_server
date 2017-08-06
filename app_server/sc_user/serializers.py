from .models import UserInfo
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        # depth = 1
        fields = ('id', 'uname', 'upwd', 'uphone')
