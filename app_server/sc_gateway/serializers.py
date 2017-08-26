from .models import GatewayInfo
from rest_framework import serializers

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayInfo
        # depth = 1
        fields = ('id', 'gname', 'gmac', 'gpasscode','gdid','guser')
