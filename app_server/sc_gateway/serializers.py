# -*- coding: utf-8 -*-
from .models import GatewayInfo
from rest_framework import serializers

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewayInfo
        fields = ('id', 'gname', 'gmac', 'gpasscode','gdid','guser')
